"""Bhashini (National Language Translation Mission - MeitY) integration.

Provides official Government of India AI4Bharat / ULCA translation (NMT)
pipeline connectivity for 22 scheduled Indian languages, enabling high-quality
bilingual and multilingual legal & regulatory assistance across English, Hindi,
Tamil, Telugu, Bengali, Marathi, Gujarati, Kannada, and more.
"""
from __future__ import annotations

import json
import logging
import os
import re
import sys
import urllib.error
import urllib.request
from typing import Any, Dict, List, Optional, Tuple

logger = logging.getLogger("ipsakti.bhashini")

BHASHINI_PIPELINE_URL = "https://meity-auth.ulcacontrib.org/ulca/apis/v0/model/getModelsPipeline"
DEFAULT_PIPELINE_ID = "64392f96daac500b55c543cd"

# Standard Bhashini / ISO language code mapping with native script names
SUPPORTED_LANGUAGES: Dict[str, Dict[str, str]] = {
    "en": {"name": "English", "native": "English", "script": "Latn"},
    "hi": {"name": "Hindi", "native": "हिन्दी", "script": "Deva"},
    "ta": {"name": "Tamil", "native": "தமிழ்", "script": "Taml"},
    "te": {"name": "Telugu", "native": "తెలుగు", "script": "Telu"},
    "bn": {"name": "Bengali", "native": "বাংলা", "script": "Beng"},
    "mr": {"name": "Marathi", "native": "मराठी", "script": "Deva"},
    "gu": {"name": "Gujarati", "native": "ગુજરાતી", "script": "Gujr"},
    "kn": {"name": "Kannada", "native": "ಕನ್ನಡ", "script": "Knda"},
    "ml": {"name": "Malayalam", "native": "മലയാളം", "script": "Mlym"},
    "pa": {"name": "Punjabi", "native": "ਪੰਜਾਬੀ", "script": "Guru"},
    "or": {"name": "Odia", "native": "ଓଡ଼ିଆ", "script": "Orya"},
    "as": {"name": "Assamese", "native": "অসমীয়া", "script": "Beng"},
    "ur": {"name": "Urdu", "native": "اردو", "script": "Arab"},
    "sa": {"name": "Sanskrit", "native": "संस्कृतम्", "script": "Deva"},
}


class BhashiniError(Exception):
    """Raised when Bhashini API returns an error or fails communication."""
    pass


class BhashiniClient:
    """Client for Bhashini MeitY / ULCA translation and Indic NLP services."""

    def __init__(
        self,
        user_id: Optional[str] = None,
        api_key: Optional[str] = None,
        inference_key: Optional[str] = None,
        pipeline_id: Optional[str] = None,
        timeout: float = 20.0,
    ) -> None:
        self._ensure_env_loaded()
        self.user_id = (user_id or os.environ.get("BHASHINI_USER_ID", "")).strip()
        self.api_key = (api_key or os.environ.get("BHASHINI_API_KEY", "")).strip()
        self.inference_key = (
            inference_key or os.environ.get("BHASHINI_INFERENCE_KEY", "")
        ).strip()
        self.pipeline_id = (
            pipeline_id
            or os.environ.get("BHASHINI_PIPELINE_ID", "")
            or DEFAULT_PIPELINE_ID
        ).strip()
        self.timeout = timeout
        self._pipeline_cache: Dict[Tuple[str, str], Dict[str, Any]] = {}

    def _ensure_env_loaded(self) -> None:
        if "pytest" in sys.modules:
            return
        try:
            from dotenv import load_dotenv
            from pathlib import Path
            cur = Path(__file__).resolve()
            for _ in range(5):
                cur = cur.parent
                env_file = cur / ".env"
                if env_file.is_file():
                    load_dotenv(env_file)
                    break
        except Exception:
            pass

    @property
    def is_configured(self) -> bool:
        """Return True if all required Bhashini credentials are present."""
        return bool(self.user_id and self.api_key and self.inference_key)

    def get_supported_languages(self) -> Dict[str, Dict[str, str]]:
        """Return the dictionary of supported Bhashini languages."""
        return dict(SUPPORTED_LANGUAGES)

    def resolve_pipeline(self, source_lang: str, target_lang: str) -> Dict[str, Any]:
        """Call getModelsPipeline to obtain serviceId and inference callback URL for a language pair."""
        cache_key = (source_lang, target_lang)
        if cache_key in self._pipeline_cache:
            return self._pipeline_cache[cache_key]

        if not self.is_configured:
            raise BhashiniError("Bhashini credentials are not fully configured in environment.")

        payload = {
            "pipelineTasks": [
                {
                    "taskType": "translation",
                    "config": {
                        "language": {
                            "sourceLanguage": source_lang,
                            "targetLanguage": target_lang,
                        }
                    },
                }
            ],
            "pipelineRequestConfig": {
                "pipelineId": self.pipeline_id,
            },
        }

        headers = {
            "userID": self.user_id,
            "ulcaApiKey": self.api_key,
            "Content-Type": "application/json",
            "User-Agent": "IP-SAKTI-Sahayak/1.0",
        }

        req = urllib.request.Request(
            BHASHINI_PIPELINE_URL,
            data=json.dumps(payload).encode("utf-8"),
            headers=headers,
            method="POST",
        )

        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                data = json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            err_body = exc.read().decode("utf-8", errors="replace")
            raise BhashiniError(f"Bhashini pipeline resolution failed ({exc.code}): {err_body}") from exc
        except Exception as exc:
            raise BhashiniError(f"Bhashini pipeline network failure: {exc}") from exc

        endpoint_info = data.get("pipelineInferenceAPIEndPoint", {})
        callback_url = endpoint_info.get("callbackUrl")
        key_header = endpoint_info.get("inferenceApiKey", {}).get("name", "Authorization")
        key_val = endpoint_info.get("inferenceApiKey", {}).get("value") or self.inference_key

        service_id = None
        for task in data.get("pipelineResponseConfig", []):
            if task.get("taskType") == "translation":
                configs = task.get("config", [])
                if configs:
                    service_id = configs[0].get("serviceId")
                    break

        if not callback_url or not service_id:
            raise BhashiniError(
                f"Bhashini pipeline returned no service for pair {source_lang} -> {target_lang}"
            )

        resolved = {
            "callback_url": callback_url,
            "service_id": service_id,
            "header_name": key_header,
            "header_value": key_val,
        }
        self._pipeline_cache[cache_key] = resolved
        return resolved

    def translate(
        self,
        text: str,
        source_lang: str = "en",
        target_lang: str = "hi",
    ) -> str:
        """Translate text between Indian languages and English using Bhashini NMT."""
        if not text or not text.strip():
            return text

        if source_lang.lower() == target_lang.lower():
            return text

        if not self.is_configured:
            logger.warning("Bhashini not configured; returning original text.")
            return text

        results = self.translate_batch([text], source_lang=source_lang, target_lang=target_lang)
        return results[0] if results else text

    def translate_batch(
        self,
        texts: List[str],
        source_lang: str = "en",
        target_lang: str = "hi",
    ) -> List[str]:
        """Translate a batch of strings using Bhashini NMT inference."""
        if not texts:
            return []

        if source_lang.lower() == target_lang.lower() or not self.is_configured:
            return texts

        try:
            pipeline = self.resolve_pipeline(source_lang, target_lang)
        except Exception as exc:
            logger.error(f"Failed to resolve Bhashini pipeline: {exc}")
            return texts

        infer_payload = {
            "pipelineTasks": [
                {
                    "taskType": "translation",
                    "config": {
                        "language": {
                            "sourceLanguage": source_lang,
                            "targetLanguage": target_lang,
                        },
                        "serviceId": pipeline["service_id"],
                    },
                }
            ],
            "inputData": {
                "input": [{"source": t} for t in texts]
            },
        }

        infer_headers = {
            "Content-Type": "application/json",
            "User-Agent": "IP-SAKTI-Sahayak/1.0",
            pipeline["header_name"]: pipeline["header_value"],
        }

        req = urllib.request.Request(
            pipeline["callback_url"],
            data=json.dumps(infer_payload).encode("utf-8"),
            headers=infer_headers,
            method="POST",
        )

        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                data = json.loads(resp.read().decode("utf-8"))
        except Exception as exc:
            logger.error(f"Bhashini inference failed: {exc}")
            return texts

        outputs: List[str] = []
        try:
            response_tasks = data.get("pipelineResponse", [])
            for task in response_tasks:
                if task.get("taskType") == "translation":
                    for item in task.get("output", []):
                        outputs.append(item.get("target", ""))
                    break
        except Exception as exc:
            logger.error(f"Failed to parse Bhashini output: {exc}")
            return texts

        if len(outputs) == len(texts):
            return outputs
        return texts


_CLIENT_INSTANCE: Optional[BhashiniClient] = None


def get_bhashini_client() -> BhashiniClient:
    """Get or instantiate the global Bhashini client singleton."""
    global _CLIENT_INSTANCE
    if _CLIENT_INSTANCE is None:
        _CLIENT_INSTANCE = BhashiniClient()
    return _CLIENT_INSTANCE


def translate_text(text: str, source_lang: str = "en", target_lang: str = "hi") -> str:
    """Convenience helper to translate text via Bhashini."""
    return get_bhashini_client().translate(text, source_lang=source_lang, target_lang=target_lang)

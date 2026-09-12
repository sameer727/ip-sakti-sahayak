"""Member 3 Phase 2 — hosted LLM client.

Plan.md Section 4.5 recommends each workstream call a hosted LLM API. This
module is M3's own minimal client (no M1/M4/M5 code): a standard
OpenAI-compatible chat-completions call, configured through environment
variables so any hosted provider or gateway works without code changes:

    M3_LLM_BASE_URL   e.g. https://api.provider.example/v1
                      (the client appends /chat/completions)
    M3_LLM_API_KEY    bearer key for the hosted API
    M3_LLM_MODEL      model name, e.g. gpt-4o-mini / glm-4.6 / etc.
    M3_LLM_TIMEOUT    optional seconds (default 60)

When these are not configured, get_llm_client() returns None and the guidance
layer falls back to its deterministic evidence-only generation mode (see
guidance.py) — the feature still works and still abstains safely, it simply
does not produce an LLM-written narrative.

Any network/HTTP/protocol failure raises LLMError, which the guidance layer
maps to status="processing_error" (never to a fabricated answer).
"""

import json
import os
import sys
import urllib.error
import urllib.request

ENV_BASE_URL = "M3_LLM_BASE_URL"
ENV_API_KEY = "M3_LLM_API_KEY"
ENV_MODEL = "M3_LLM_MODEL"
ENV_TIMEOUT = "M3_LLM_TIMEOUT"

DEFAULT_TIMEOUT = 60
USER_AGENT = "ip-sakti-sahayak-member3/2.0"


class LLMError(Exception):
    """Raised when the hosted LLM call fails (network, HTTP, protocol)."""


class HostedLLM:
    """Minimal OpenAI-compatible chat-completions client."""

    def __init__(self, base_url, api_key, model, timeout=DEFAULT_TIMEOUT):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.model = model
        self.timeout = timeout

    def complete(self, system, user):
        """One chat completion. Returns the assistant message text.
        Raises LLMError on any failure."""
        url = self.base_url + "/chat/completions"
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "temperature": 0.0,
            "max_tokens": 1200,
        }
        request = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer " + self.api_key,
                "User-Agent": USER_AGENT,
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                body = response.read().decode("utf-8", errors="replace")
        except urllib.error.HTTPError as error:
            detail = ""
            try:
                detail = error.read().decode("utf-8", errors="replace")[:200]
            except Exception:
                pass
            raise LLMError("HTTP %s from hosted LLM: %s" % (error.code, detail)) from error
        except Exception as error:
            raise LLMError("hosted LLM call failed: %s" % error) from error

        try:
            data = json.loads(body)
            return data["choices"][0]["message"]["content"]
        except (ValueError, KeyError, IndexError, TypeError) as error:
            raise LLMError("unexpected hosted LLM response shape: %s" % error) from error


def get_llm_client(environ=None):
    """Build a HostedLLM from environment configuration, or None when the
    variables are absent/incomplete. Never raises."""
    if environ is None and "pytest" not in sys.modules and len(os.environ) > 0:
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
            else:
                load_dotenv()
        except Exception:
            pass

    env = environ if environ is not None else os.environ
    api_key = env.get(ENV_API_KEY, "").strip()

    # Fallback to shared keys only when explicitly enabled
    if not api_key and env.get("ENABLE_M3_HOSTED_LLM", "").lower() in ("1", "true", "yes"):
        api_key = (
            env.get("EXPLABS_API_KEY", "").strip()
            or env.get("LLM_API_KEY", "").strip()
            or env.get("OPENAI_API_KEY", "").strip()
            or env.get("GROQ_API_KEY", "").strip()
            or env.get("GEMINI_API_KEY", "").strip()
            or env.get("OPENROUTER_API_KEY", "").strip()
        )
        if not api_key and env.get("FREE_API", "").lower() in ("1", "true", "yes"):
            api_key = "free-local-key"

    if not api_key:
        return None

    base_url = (env.get(ENV_BASE_URL, "").strip() or env.get("LLM_BASE_URL", "").strip())
    model = (env.get(ENV_MODEL, "").strip() or env.get("LLM_MODEL", "").strip())

    if model == "gpt-5.6-luna" or (base_url and "experientiallabs.ai" in base_url):
        base_url = base_url or "https://api.experientiallabs.ai/v1"
        model = "gpt-5.6-luna"
    else:
        if not base_url:
            if env.get("GROQ_API_KEY"):
                base_url = "https://api.groq.com/openai/v1"
            elif env.get("OPENROUTER_API_KEY"):
                base_url = "https://openrouter.ai/api/v1"
            elif env.get("GEMINI_API_KEY"):
                base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
            elif env.get("FREE_API", "").lower() in ("1", "true", "yes"):
                base_url = "http://127.0.0.1:8001/v1"
            else:
                base_url = "https://api.openai.com/v1"

        if not model:
            if "experientiallabs.ai" in base_url or env.get("EXPLABS_API_KEY"):
                model = "gpt-5.6-luna"
            elif "openrouter" in base_url:
                model = "minimax/minimax-m3:free"
            elif "googleapis" in base_url:
                model = "gemini-3.6-flash"
            elif "groq" in base_url:
                model = "llama-3.3-70b-versatile"
            elif env.get("FREE_API", "").lower() in ("1", "true", "yes"):
                model = "free-ayurveda-llm"
            else:
                model = "gpt-4o-mini"

    if not (base_url and api_key and model):
        return None
    try:
        timeout = float(env.get(ENV_TIMEOUT, "") or env.get("LLM_TIMEOUT_SECS", "") or DEFAULT_TIMEOUT)
    except ValueError:
        timeout = DEFAULT_TIMEOUT
    return HostedLLM(base_url, api_key, model, timeout=timeout)

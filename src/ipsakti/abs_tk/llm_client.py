"""Member 4 Phase 2 — LLM transport layer.

Two modes, selected from environment variables (never faked):

- HostedLLM: a real OpenAI-compatible chat-completions client (urllib, no
  SDK dependency). Enabled only when M4_LLM_API_KEY is set; base URL and
  model are configurable via M4_LLM_BASE_URL / M4_LLM_MODEL.
- Stand-in (offline): when no credentials are configured, guidance.py
  composes the answer deterministically from the retrieved evidence records
  via the same validation path. This is NOT an LLM and is never presented as
  one; the phase report documents that no live API call was made.

The hosted client is deliberately thin: it sends the constrained prompt and
returns raw text. All grounding/citation/safety validation happens in
guidance.py regardless of mode.
"""

import json
import os
import ssl
import sys
import urllib.request

API_KEY_ENV = "M4_LLM_API_KEY"
BASE_URL_ENV = "M4_LLM_BASE_URL"
MODEL_ENV = "M4_LLM_MODEL"

DEFAULT_BASE_URL = "https://api.openai.com/v1"
DEFAULT_MODEL = "gpt-4o-mini"

_SSL_CONTEXT = ssl.create_default_context()


class HostedLLM:
    """OpenAI-compatible chat-completions client (implemented, used only when
    credentials exist)."""

    def __init__(self, api_key, model=None, base_url=None):
        self.api_key = api_key
        self.model = model or os.environ.get(MODEL_ENV, DEFAULT_MODEL)
        self.base_url = (base_url or os.environ.get(BASE_URL_ENV, DEFAULT_BASE_URL)).rstrip("/")

    def build_payload(self, system, user, temperature=0.0):
        """Build the request body (pure, unit-testable, no network)."""
        return {
            "model": self.model,
            "temperature": temperature,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
        }

    def complete(self, system, user, timeout=60):
        payload = self.build_payload(system, user)
        req = urllib.request.Request(
            self.base_url + "/chat/completions",
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}",
            },
            method="POST",
        )
        kwargs = {"timeout": timeout}
        if self.base_url.startswith("https:"):
            kwargs["context"] = _SSL_CONTEXT
        with urllib.request.urlopen(req, **kwargs) as resp:
            body = json.loads(resp.read().decode("utf-8"))
        return body["choices"][0]["message"]["content"]


class StandInLLM:
    """Marker for the deterministic offline mode (no network, no LLM)."""

    is_llm = False


def get_llm_client(env=None):
    """Return (mode, client). mode is 'hosted' or 'stand-in'.

    Reads os.environ unless an explicit mapping is passed (used by tests).
    """
    if env is None and "pytest" not in sys.modules and len(os.environ) > 0:
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

    env = os.environ if env is None else env
    api_key = env.get(API_KEY_ENV)

    # Fallback to shared keys only when explicitly enabled
    if not api_key and env.get("ENABLE_M4_HOSTED_LLM", "").lower() in ("1", "true", "yes"):
        api_key = (
            env.get("EXPLABS_API_KEY")
            or env.get("LLM_API_KEY")
            or env.get("OPENAI_API_KEY")
            or env.get("GROQ_API_KEY")
            or env.get("GEMINI_API_KEY")
            or env.get("OPENROUTER_API_KEY")
        )
        if not api_key and env.get("FREE_API", "").lower() in ("1", "true", "yes"):
            api_key = "free-local-key"

    if api_key:
        model = env.get(MODEL_ENV) or env.get("LLM_MODEL")
        base_url = env.get(BASE_URL_ENV) or env.get("LLM_BASE_URL")

        if model == "gpt-5.6-luna" or (base_url and "experientiallabs.ai" in base_url):
            base_url = base_url or "https://api.experientiallabs.ai/v1"
            model = "gpt-5.6-luna"
            return "hosted", HostedLLM(api_key, model=model, base_url=base_url)

        if not base_url:
            if env.get("GROQ_API_KEY"):
                base_url = "https://api.groq.com/openai/v1"
            elif env.get("GEMINI_API_KEY"):
                base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
            elif env.get("OPENROUTER_API_KEY"):
                base_url = "https://openrouter.ai/api/v1"
            elif env.get("FREE_API", "").lower() in ("1", "true", "yes"):
                base_url = "http://127.0.0.1:8001/v1"

        if not model:
            if env.get("GROQ_API_KEY"):
                model = "llama-3.3-70b-versatile"
            elif env.get("GEMINI_API_KEY"):
                model = "gemini-3.6-flash"
            elif env.get("OPENROUTER_API_KEY"):
                model = "minimax/minimax-m3:free"
            elif env.get("FREE_API", "").lower() in ("1", "true", "yes"):
                model = "free-ayurveda-llm"

        return "hosted", HostedLLM(api_key, model=model, base_url=base_url)
    return "stand-in", StandInLLM()

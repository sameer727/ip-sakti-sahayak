"""Runtime configuration for M1 (environment-driven; no secrets in code).

The assistant picks a hosted LLM API per Plan.md §4.5 (no self-hosting). Any
OpenAI-compatible chat-completions endpoint works: point LLM_BASE_URL/LLM_MODEL
at the provider and set LLM_API_KEY. When no key is configured the assistant
falls back to a deterministic extractive generator so the pipeline stays
runnable and testable without credentials; it never fabricates content.
"""
from __future__ import annotations

import os
import sys
from dataclasses import dataclass

DISCLAIMER_EN = (
    "Disclaimer: IP-SAKTI Sahayak provides general legal information, not legal "
    "advice. Answers are generated from a small curated corpus of public sources "
    "(corpus reference: August 2026) and may be incomplete or outdated. Verify "
    "against official sources and consult a qualified IP professional before acting."
)
DISCLAIMER_HI = (
    "अस्वीकरण: IP-SAKTI सहायक सामान्य कानूनी जानकारी देता है, यह कानूनी सलाह नहीं है। "
    "उत्तर सार्वजनिक स्रोतों के एक छोटे चुनिंदा संग्रह (संदर्भ: अगस्त 2026) से तैयार "
    "किए जाते हैं और अपूर्ण या पुराने हो सकते हैं। कोई भी कदम उठाने से पहले आधिकारिक "
    "स्रोतों से जानकारी सत्यापित करें और योग्य विशेषज्ञ से परामर्श लें।"
)

FALLBACK_EN = (
    "I could not find relevant information in my curated corpus for this "
    "question, so I will not guess. Please rephrase the question, consult the "
    "official sources directly (IP India — ipindia.gov.in, India Code — "
    "indiacode.nic.in, WIPO — wipo.int), or speak to a qualified professional."
)
FALLBACK_HI = (
    "मेरे चुनिंदा स्रोत-संग्रह में इस प्रश्न से संबंधित जानकारी नहीं मिली, इसलिए मैं "
    "अनुमान नहीं लगाऊंगा। कृपया प्रश्न दूसरे शब्दों में पूछें, आधिकारिक स्रोत देखें "
    "(IP India — ipindia.gov.in, India Code — indiacode.nic.in, WIPO — wipo.int) "
    "या योग्य विशेषज्ञ से परामर्श लें।"
)

SPECIALIST_UNAVAILABLE_EN = (
    "This question belongs to the {domain} specialist domain, and that "
    "specialist capability is not available in this build. Per the assistant's "
    "corpus-safety rule it will not substitute unrelated general-corpus "
    "evidence for the missing specialist. Please consult official sources "
    "directly or try again once the specialist domain is wired in."
)
SPECIALIST_UNAVAILABLE_HI = (
    "यह प्रश्न {domain} विशेषज्ञ डोमेन से संबंधित है, और वह विशेषज्ञ क्षमता इस "
    "बिल्ड में उपलब्ध नहीं है। सहायक के स्रोत-सुरक्षा नियम के अनुसार यह असंबंधित "
    "सामान्य स्रोत-सामग्री से उत्तर नहीं देगा। कृपया सीधे आधिकारिक स्रोत देखें या "
    "विशेषज्ञ डोमेन जुड़ने के बाद फिर प्रयास करें।"
)


@dataclass
class Config:
    llm_api_key: str = ""
    llm_base_url: str = "https://api.openai.com/v1"
    llm_model: str = "gpt-4o-mini"
    llm_timeout_secs: float = 30.0
    retrieval_top_k: int = 3
    # Raw retrieval score below which the assistant treats the corpus as having
    # no relevant evidence at all (retrieval floor).
    min_evidence_score: float = 0.5
    # Evidence-sufficiency threshold (Phase 2): the top ranked evidence must
    # reach this raw score for the assistant to answer. Evidence between the
    # retrieval floor and this threshold triggers abstention, not a guess.
    sufficiency_threshold: float = 2.5
    # Corpus-safety seam (MEMBER_1.md §3): when True, a query routed to a
    # specialist domain with no registered specialist must abstain instead of
    # silently answering from M1's standalone demo corpus. Stays False during
    # standalone Phase 1–3 development so the demo path works; M6 flips it when
    # M2–M5 are wired in.
    specialists_wired: bool = False

    @property
    def generator_mode(self) -> str:
        return "llm" if self.llm_api_key else "extractive"


def _load_env_file() -> None:
    if "pytest" in sys.modules:
        return
    if len(os.environ) == 0:
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
        else:
            load_dotenv()
    except Exception:
        pass


def load_config() -> Config:
    _load_env_file()

    api_key = (
        os.environ.get("LLM_API_KEY")
        or os.environ.get("OPENAI_API_KEY")
        or os.environ.get("GROQ_API_KEY")
        or os.environ.get("GEMINI_API_KEY")
        or os.environ.get("OPENROUTER_API_KEY")
        or ""
    ).strip()

    is_free_local = os.environ.get("FREE_API", "").lower() in ("1", "true", "yes")
    if not api_key and is_free_local:
        api_key = "free-local-key"

    default_base_url = "https://api.openai.com/v1"
    default_model = "gpt-4o-mini"

    # Pre-configured free tier and gateway provider presets
    if os.environ.get("EXPLABS_API_KEY") or os.environ.get("LLM_MODEL") == "gpt-5.6-luna":
        default_base_url = "https://api.experientiallabs.ai/v1"
        default_model = "gpt-5.6-luna"
    elif os.environ.get("GROQ_API_KEY"):
        default_base_url = "https://api.groq.com/openai/v1"
        default_model = "llama-3.3-70b-versatile"
    elif os.environ.get("GEMINI_API_KEY"):
        default_base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
        default_model = "gemini-3.6-flash"
    elif os.environ.get("OPENROUTER_API_KEY"):
        default_base_url = "https://openrouter.ai/api/v1"
        default_model = "minimax/minimax-m3:free"
    elif is_free_local:
        default_base_url = "http://127.0.0.1:8001/v1"
        default_model = "free-ayurveda-llm"

    base_url = os.environ.get("LLM_BASE_URL") or default_base_url
    model = os.environ.get("LLM_MODEL") or default_model

    if model == "gpt-5.6-luna" or "experientiallabs.ai" in base_url:
        base_url = os.environ.get("LLM_BASE_URL") or "https://api.experientiallabs.ai/v1"
        api_key = os.environ.get("EXPLABS_API_KEY", "").strip()
        if not api_key:
            # Fall back to alternative keys if available
            api_key = (
                os.environ.get("OPENROUTER_API_KEY", "")
                or os.environ.get("GEMINI_API_KEY", "")
                or os.environ.get("GROQ_API_KEY", "")
                or os.environ.get("OPENAI_API_KEY", "")
                or ""
            ).strip()
    elif "openrouter" in base_url and os.environ.get("OPENROUTER_API_KEY"):
        api_key = os.environ.get("OPENROUTER_API_KEY", "").strip()
    elif "googleapis" in base_url and os.environ.get("GEMINI_API_KEY"):
        api_key = os.environ.get("GEMINI_API_KEY", "").strip()
    elif "groq" in base_url and os.environ.get("GROQ_API_KEY"):
        api_key = os.environ.get("GROQ_API_KEY", "").strip()
    elif "openai.com" in base_url and os.environ.get("OPENAI_API_KEY"):
        api_key = os.environ.get("OPENAI_API_KEY", "").strip()
    elif ("127.0.0.1" in base_url or "localhost" in base_url) and not api_key:
        api_key = "free-local-key"

    return Config(
        llm_api_key=api_key,
        llm_base_url=base_url,
        llm_model=model,
        llm_timeout_secs=float(os.environ.get("LLM_TIMEOUT_SECS", "60")),
        retrieval_top_k=int(os.environ.get("RETRIEVAL_TOP_K", "3")),
        min_evidence_score=float(os.environ.get("MIN_EVIDENCE_SCORE", "0.5")),
        sufficiency_threshold=float(os.environ.get("SUFFICIENCY_THRESHOLD", "2.5")),
        specialists_wired=os.environ.get("SPECIALISTS_WIRED", "").lower()
        in ("1", "true", "yes"),
    )


_config: Config | None = None


def get_config() -> Config:
    global _config
    if _config is None:
        _config = load_config()
    return _config


def set_config(cfg: Config) -> None:
    """Replace the process config (used by tests and the demo script)."""
    global _config
    _config = cfg


def reset_config() -> None:
    """Drop the cached config so the next get_config() reloads from env."""
    global _config
    _config = None

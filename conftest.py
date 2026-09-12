"""Root pytest bootstrap for IP-SAKTI Sahayak.
Ensures all canonical ipsakti packages are aliased to legacy names in sys.modules
for seamless test discovery across the unified tests/ suite.
"""
import importlib
import os
import pkgutil
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent
_SRC_DIR = _REPO_ROOT / "src"

if str(_SRC_DIR) not in sys.path:
    sys.path.insert(0, str(_SRC_DIR))
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))
_ABS_TK_TESTS = _REPO_ROOT / "tests" / "abs_tk"
if str(_ABS_TK_TESTS) not in sys.path:
    sys.path.insert(0, str(_ABS_TK_TESTS))

# Ensure offline extractive mode per contract
for _k in ("EXPLABS_API_KEY", "OPENROUTER_API_KEY", "GEMINI_API_KEY", "GROQ_API_KEY", "OPENAI_API_KEY", "LLM_API_KEY", "LLM_BASE_URL", "LLM_MODEL"):
    os.environ.pop(_k, None)


def _bind_module_alias(alias_name: str, target_module) -> None:
    sys.modules[alias_name] = target_module
    if hasattr(target_module, "__path__"):
        for info in pkgutil.iter_modules(target_module.__path__):
            try:
                sub = importlib.import_module(f"{target_module.__name__}.{info.name}")
                sys.modules[f"{alias_name}.{info.name}"] = sub
            except Exception:
                pass


def setup_package_aliases() -> None:
    try:
        import ipsakti.core
        import ipsakti.classifier
        import ipsakti.india_ip
        import ipsakti.abs_tk
        import ipsakti.international_ip
        import ipsakti.integration

        # Bind m1 -> ipsakti.core
        _bind_module_alias("m1", ipsakti.core)
        _bind_module_alias("sihmember1.m1", ipsakti.core)

        # Bind member2 & sihmember2 -> ipsakti.classifier
        _bind_module_alias("member2", ipsakti.classifier)
        _bind_module_alias("sihmember2", ipsakti.classifier)

        # Bind member3 & sihmember3 -> ipsakti.india_ip
        _bind_module_alias("member3", ipsakti.india_ip)
        _bind_module_alias("sihmember3", ipsakti.india_ip)

        # Bind member5 & sihmember5.member5 -> ipsakti.international_ip
        _bind_module_alias("member5", ipsakti.international_ip)
        _bind_module_alias("sihmember5.member5", ipsakti.international_ip)

        # Bind integration -> ipsakti.integration
        _bind_module_alias("integration", ipsakti.integration)

        # Bind ABS/TK flat modules
        for name in ("corpus", "guidance", "hindi", "llm_client", "retrieval"):
            try:
                mod = importlib.import_module(f"ipsakti.abs_tk.{name}")
                sys.modules[name] = mod
            except Exception:
                pass
    except Exception as exc:
        print(f"Warning during alias setup: {exc}")


setup_package_aliases()

import pytest


@pytest.fixture(autouse=True)
def reset_m1_specialists(request):
    """Ensure core standalone tests run in clean standalone state without leakage from integration wiring."""
    if "core" in str(request.fspath) or "sihmember1" in str(request.fspath):
        try:
            from ipsakti.core import routing, assistant
            saved_specialists = dict(routing._SPECIALISTS)
            saved_handlers = dict(assistant._SPECIALIST_HANDLERS)
            routing._SPECIALISTS.clear()
            assistant._SPECIALIST_HANDLERS.clear()
            yield
            routing._SPECIALISTS.clear()
            routing._SPECIALISTS.update(saved_specialists)
            assistant._SPECIALIST_HANDLERS.clear()
            assistant._SPECIALIST_HANDLERS.update(saved_handlers)
            return
        except ImportError:
            pass
    yield

"""IP-SAKTI Sahayak: AI-Powered Intellectual Property & Regulatory Assistant.

Enterprise modular packages:
- ipsakti.core: Core orchestration, routing, API, and retrieval
- ipsakti.classifier: Formulation classification engine
- ipsakti.india_ip: India IP & regulatory guidance
- ipsakti.abs_tk: Access & Benefit Sharing and Traditional Knowledge
- ipsakti.international_ip: International IP guidance
- ipsakti.integration: Multi-agent assembly, semantic synthesis, and contracts
"""

__version__ = "1.0.0"
__author__ = "IP-SAKTI Sahayak Team"

from . import abs_tk, classifier, core, india_ip, integration, international_ip

__all__ = [
    "core",
    "classifier",
    "india_ip",
    "abs_tk",
    "international_ip",
    "integration",
    "__version__",
]

"""IP-SAKTI Sahayak: Access & Benefit Sharing (ABS) & Traditional Knowledge (TK) Specialist.

Provides authoritative statutory guidance on the Biological Diversity Act 2002,
NBA approvals, SBB intimations, Prior Informed Consent (PIC), Mutually Agreed Terms (MAT),
and Traditional Knowledge Digital Library (TKDL) references.
"""

from .guidance import (
    DOMAIN_ABS,
    DOMAIN_OTHER_IP,
    DOMAIN_TK,
    DOMAIN_UNCLEAR,
    Relevance,
    answer,
    classify_query,
    get_evidence,
)
from .retrieval import retrieve
from .corpus import SOURCE_RECORDS, CORPUS_VERSION

__version__ = "1.0.0"

__all__ = [
    "answer",
    "classify_query",
    "get_evidence",
    "retrieve",
    "Relevance",
    "DOMAIN_ABS",
    "DOMAIN_TK",
    "DOMAIN_OTHER_IP",
    "DOMAIN_UNCLEAR",
    "SOURCE_RECORDS",
    "CORPUS_VERSION",
    "__version__",
]


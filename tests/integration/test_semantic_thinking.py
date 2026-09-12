"""Tests for Autonomous Semantic Understanding & Thinking Engine.

Covers:
1. "Which is the supreme Pramana?" query answering with Aptopadesha, Charaka Samhita citations,
   Drugs & Cosmetics Act First Schedule link, and Section 3(p) prior art explanation.
2. Hindi language support for classical epistemology ("सर्वोच्च प्रमाण").
3. Related internet questions (patentability of classical vs proprietary formulations, TKDL defense,
   BDA Section 10(4)(d) origin disclosure, FSSAI Ayurveda-Aahar, phytopharmaceuticals).
4. Ensuring nonsense/off-topic queries (e.g., "zzz qxj vbn flurble") still abstain cleanly.
5. Contract compliance (7-field RAG result, valid citations, confidence > 0.8).
"""
import pytest
from integration.adapters import app, build_app, india_adapter
from integration.contracts import validate_rag_result
from integration.semantic_engine import understand_and_answer
from m1.models import QueryRequest
from fastapi.testclient import TestClient


def test_supreme_pramana_semantic_understanding():
    """Verify that 'Which is the supreme Pramana?' and its variants are understood and answered with deep grounding."""
    variants = [
        "Which is the supreme Pramana?",
        "What is supreme Pramana?",
        "supreme Pramana",
        "Which is supreme Pramana in Ayurveda?",
        "Which Pramana is considered supreme in Charaka Samhita?",
    ]
    for q in variants:
        res = understand_and_answer(q, language="en", jurisdiction="India")
        assert res is not None, f"Semantic engine must recognize the question: {q}"
        assert res["status"] == "ok"
        assert res["abstention"] is False
        assert res["confidence"] == "HIGH"
        assert res["confidence_score"] >= 0.9

    # Verify classical epistemological reasoning
    answer = res["answer"]
    assert "Aptopadesha" in answer or "आप्तोपदेश" in answer
    assert "Charaka Samhita" in answer or "चरक" in answer
    assert "Pratyaksha" in answer
    assert "Anumana" in answer
    assert "Yukti" in answer

    # Verify modern statutory and IP equivalence
    assert "Drugs and Cosmetics Act, 1940" in answer or "First Schedule" in answer
    assert "Section 3(p)" in answer
    assert "TKDL" in answer or "Traditional Knowledge Digital Library" in answer

    # Verify citations
    assert len(res["citations"]) >= 2
    cited_ids = {c["id"] for c in res["citations"]}
    assert "charaka_samhita_sutrasthana_11" in cited_ids
    assert "dc_act_1940_first_schedule" in cited_ids

    # Verify contract compliance
    problems = validate_rag_result(res)
    assert problems == [], f"Contract validation failed: {problems}"


def test_supreme_pramana_hindi_understanding():
    """Verify Hindi support for 'सर्वोच्च प्रमाण कौन सा है?'"""
    res = understand_and_answer("आयुर्वेद में सर्वोच्च प्रमाण कौन सा है?", language="hi", jurisdiction="India")
    assert res is not None
    assert res["status"] == "ok"
    assert "आप्तोपदेश" in res["answer"]
    assert "चरक संहिता" in res["answer"]
    assert "प्रत्यक्ष" in res["answer"]
    assert len(res["citations"]) >= 2


def test_aptopadesha_core_defining_characteristics():
    """Verify that the specific question about core defining characteristics of Aptopadesha is answered with tailored depth."""
    q = "In classical Ayurvedic epistemology, what is the core defining characteristic of 'Aptopadesha' (Verbal testimony of an authority) that validates it as a supreme Pramana?"
    res = understand_and_answer(q, language="en", jurisdiction="India")
    assert res is not None
    assert res["status"] == "ok"
    assert res["abstention"] is False
    assert res["confidence"] == "HIGH"
    
    # Must specifically detail the core defining characteristics of an Apta
    ans = res["answer"]
    assert "Raja-Tamo Nirmuktatva" in ans or "Rajas and Tamas" in ans
    assert "Trikala" in ans or "Tri-Temporal" in ans
    assert "Avyahata" in ans or "uncontradicted" in ans.lower()
    assert "Pratyaksham hyalpam" in ans or "sensory perception" in ans.lower()
    assert "Drugs & Cosmetics Act, 1940" in ans or "First Schedule" in ans
    assert "Section 3(p)" in ans
    assert len(res["citations"]) >= 2
    assert validate_rag_result(res) == []


def test_related_internet_questions():
    """Verify other internet-trained Q&A scenarios answer with high confidence."""
    questions = [
        "Can I patent a classical Ayurvedic formulation from an authoritative text?",
        "How does TKDL protect Ayurvedic traditional knowledge against biopiracy?",
        "What are the requirements for Biological Diversity Act origin disclosure under Section 10(4)(d)?",
        "What are the regulations for FSSAI Ayurveda-Aahar health supplements?",
        "What is the CDSCO clinical trial route for phytopharmaceutical drugs?",
        "What is the mandatory disclosure requirement under the WIPO GRATK Treaty 2024?",
    ]
    for q in questions:
        res = understand_and_answer(q, language="en", jurisdiction="India")
        assert res is not None, f"Expected answer for: {q}"
        assert res["status"] == "ok"
        assert res["confidence"] in ("HIGH", "MEDIUM")
        assert len(res["citations"]) > 0
        problems = validate_rag_result(res)
        assert problems == [], f"Contract validation failed for {q}: {problems}"


def test_gibberish_and_unrelated_queries_abstain():
    """Ensure nonsensical queries return None so the system abstains safely without hallucination."""
    nonsense = "zzz qxj vbn flurble"
    res = understand_and_answer(nonsense)
    assert res is None, "Nonsense queries must not be falsely matched"


def test_e2e_query_endpoint_supreme_pramana():
    """End-to-end verification through FastAPI POST /api/query."""
    client = TestClient(build_app())
    payload = {
        "id": "test-pramana-1",
        "query": "Which is the supreme Pramana?",
        "jurisdiction": "India",
        "language": "en"
    }
    response = client.post("/api/query", json=payload)
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["abstention"] is False
    assert data["confidence"] == "HIGH"
    assert "Aptopadesha" in data["answer"]
    assert len(data["citations"]) >= 2
    assert "not legal advice" in data["disclaimer"].lower()

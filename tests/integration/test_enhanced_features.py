"""Automated tests for enhanced features (SIH-26045):
- GIS & Remote Sensing Ayurveda Geo-Origin data
- Interactive Knowledge Graph schema & integrity
- Statutory Forms & Registry fee calculator & URLs
- Human IP Facilitator Escalation Desk (AIIA-ICAINE)
- DPDP Act 2023 & MeitY AI Advisory Audit Logger
"""
import pytest
from fastapi.testclient import TestClient

from integration.adapters import app


@pytest.fixture(scope="module")
def client():
    return TestClient(app)


def test_gis_data_endpoint(client):
    response = client.get("/api/gis/data")
    assert response.status_code == 200
    data = response.json()
    assert "gis_records" in data
    assert "sbb_directory" in data
    assert data["total_count"] >= 7
    
    # Verify core GIs from Research.md are present
    gi_names = [r["name"] for r in data["gis_records"]]
    assert any("Ashwagandha" in n for n in gi_names)
    assert any("Navara" in n for n in gi_names)
    assert any("Lakadong" in n for n in gi_names)
    assert any("Saffron" in n for n in gi_names)
    assert any("Cardamom" in n for n in gi_names)
    
    # Check coordinates and remote sensing metadata
    for record in data["gis_records"]:
        assert len(record["coordinates"]) == 2
        assert -90 <= record["coordinates"][0] <= 90
        assert -180 <= record["coordinates"][1] <= 180
        assert "remote_sensing" in record
        rs = record["remote_sensing"]
        assert "altitude_meters" in rs
        assert "soil_type" in rs
        assert "annual_rainfall_mm" in rs


def test_knowledge_graph_endpoint(client):
    response = client.get("/api/knowledge-graph")
    assert response.status_code == 200
    data = response.json()
    assert "nodes" in data
    assert "links" in data
    assert len(data["nodes"]) >= 20
    assert len(data["links"]) >= 15
    
    node_types = {n["type"] for n in data["nodes"]}
    assert "formulation" in node_types
    assert "regime" in node_types
    assert "caselaw" in node_types
    assert "authority" in node_types
    assert "treaty" in node_types
    
    # Verify landmark case law from Research.md
    node_labels = [n["label"] for n in data["nodes"]]
    assert any("Zero Brand Zone" in l for l in node_labels)
    assert any("Shaafi Naturcure" in l for l in node_labels)
    assert any("Turmeric" in l for l in node_labels)


def test_forms_directory_endpoint(client):
    response = client.get("/api/forms")
    assert response.status_code == 200
    data = response.json()
    assert "forms" in data
    assert data["total_count"] >= 8
    
    form_codes = [f["code"] for f in data["forms"]]
    assert any("Form 1" in c for c in form_codes)
    assert any("Form GI-1" in c for c in form_codes)
    assert any("Form TM-A" in c for c in form_codes)
    assert any("FoSCoS" in c for c in form_codes)
    assert any("WIPO" in f["admin_body"] or "PCT" in c for f in data["forms"] for c in [f["code"]])
    
    for f in data["forms"]:
        assert f["portal_url"].startswith("http")
        assert "fees" in f


def test_human_escalation_endpoint(client):
    payload = {
        "query": "Is my novel extraction method for Ashwagandha patentable without SBB penalty?",
        "jurisdiction": "India",
        "formulation_class": "Proprietary",
        "user_name": "Dr. Ananya Roy",
        "user_email": "ananya.roy@ayushresearch.in",
        "user_phone": "+91 9876543210",
        "user_organization": "National Ayurveda Research Lab",
        "details": "We have an ultrasonic extraction process showing 4x bioavailability.",
        "citations": [{"source_name": "The Patents Act, 1970", "section": "Section 3(p)"}],
    }
    response = client.post("/api/escalate", json=payload)
    assert response.status_code == 200
    ticket = response.json()
    assert ticket["status"] == "submitted"
    assert ticket["ticket_id"].startswith("AIIA-IP-")
    assert "Ministry of Ayush / AIIA-ICAINE" in ticket["assigned_desk"]
    assert ticket["expected_response_hours"] == 48


def test_dpdp_audit_trail_endpoint(client):
    response = client.get("/api/audit-trail?limit=10")
    assert response.status_code == 200
    data = response.json()
    assert "logs" in data
    assert data["dpdp_aligned"] is True
    assert len(data["logs"]) >= 1
    
    latest = data["logs"][0]
    assert "id" in latest
    assert "timestamp" in latest
    assert "data_localisation" in latest

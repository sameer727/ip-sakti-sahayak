"""Frontend-serving regression tests (demo frontend, M6 Phase 4).

The frontend is a static vanilla HTML/CSS/JS app served by the integrated
backend itself (same origin — no CORS, one process). These tests pin the
connection points:

- GET /api/classify/questions exposes Member 2's own get_questions() data
  (the guided UI renders from this — never hardcoded question text);
- GET / serves the frontend index.html;
- static assets (css/js) are served;
- the /api contract endpoints are unaffected by the static mount.
"""
import pytest
from fastapi.testclient import TestClient

from integration.adapters import wire_m1


@pytest.fixture(scope="module")
def client():
    wire_m1()
    from integration.adapters import app

    return TestClient(app)


def test_index_html_served(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "IP-SAKTI Sahayak" in response.text
    assert "text/html" in response.headers["content-type"]


def test_static_assets_served(client):
    for path in ("/css/styles.css", "/js/api.js", "/js/app.js", "/js/classifier.js"):
        response = client.get(path)
        assert response.status_code == 200, path
    assert "text/css" in client.get("/css/styles.css").headers["content-type"]
    assert "javascript" in client.get("/js/app.js").headers["content-type"]


def test_classify_questions_endpoint(client):
    """The questions endpoint returns Member 2's REAL bilingual question set —
    exactly what get_questions() exposes, no duplicated definitions."""
    response = client.get("/api/classify/questions")
    assert response.status_code == 200
    body = response.json()
    assert body["jurisdictions"] == ["India", "International"]
    assert body["languages"] == ["en", "hi"]
    assert set(body["categories"]) == {
        "Classical", "Proprietary", "Phytopharmaceutical", "Ayurveda-Aahar",
        "Cosmetic", "New Drug", "Uncertain"}
    questions = body["questions"]
    assert len(questions) == 6
    for question in questions:
        assert question["id"] and question["text"] and question["text_hi"]
        assert question["options"] and question["options_hi"]
        assert set(question["options"]) == set(question["options_hi"])
    known_ids = {q["id"] for q in questions}
    assert known_ids == {
        "primary_purpose", "food_exclusion", "text_source",
        "standardised_fraction", "ingredients_known", "new_indication"}


def test_questions_are_the_real_m2_data(client):
    """Endpoint output must equal a live get_questions() call (deep equality),
    proving the UI renders the real classifier data source."""
    from integration.adapters import load_members

    m2 = load_members()["m2"]["pkg"]
    served = client.get("/api/classify/questions").json()["questions"]
    assert served == m2.get_questions()


def test_api_endpoints_unaffected_by_static_mount(client):
    assert client.get("/api/health").status_code == 200
    response = client.post("/api/query", json={
        "id": "fe-1",
        "query": "I want to file a patent for a new Ayurvedic drug outside India - what route do I use?",
        "language": "en", "jurisdiction": "International"})
    assert response.status_code == 200
    assert response.json()["abstention"] is False


def test_indic_multilingual_frontend_internationalization(client):
    """Verify that index.html contains all 22 scheduled Indic languages in moreIndicLangSelect,
    the Bhashini badge, language toggle, and that assets load properly."""
    res = client.get("/")
    assert res.status_code == 200
    html = res.text

    # 1. Check quick toggle for English and Hindi
    assert 'id="languageToggle"' in html
    assert 'data-value="en"' in html
    assert 'data-value="hi"' in html

    # 2. Check Bhashini badge and spinner
    assert 'badge-bhashini' in html
    assert 'id="langSpinner"' in html

    # 3. Check moreIndicLangSelect and all 22 scheduled languages
    assert 'id="moreIndicLangSelect"' in html
    scheduled_22 = [
        "as", "bn", "brx", "doi", "gu", "hi", "kn", "ks", "kok", "mai",
        "ml", "mni", "mr", "ne", "or", "pa", "sa", "sat", "sd", "ta", "te", "ur"
    ]
    for code in scheduled_22:
        assert f'value="{code}"' in html, f"Missing scheduled language {code} in moreIndicLangSelect"

    # 4. Check i18n.js and styles.css content
    i18n_res = client.get("/js/i18n.js")
    assert i18n_res.status_code == 200
    assert "applyAsync" in i18n_res.text
    assert "/api/bhashini/ui-bundle" in i18n_res.text
    assert "localStorage" in i18n_res.text

    css_res = client.get("/css/styles.css")
    assert css_res.status_code == 200
    assert ".select-indic" in css_res.text
    assert ".lang-spinner" in css_res.text
    assert "@media (max-width: 768px)" in css_res.text


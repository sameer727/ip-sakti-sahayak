"""Tests for Bhashini (National Language Translation Mission - MeitY) integration."""
from __future__ import annotations

import json
from unittest.mock import MagicMock, patch

import pytest
from fastapi.testclient import TestClient

from ipsakti.core.bhashini import (
    BhashiniClient,
    BhashiniError,
    SUPPORTED_LANGUAGES,
    get_bhashini_client,
    translate_text,
)
from ipsakti.integration.adapters import app


def test_bhashini_supported_languages():
    client = BhashiniClient()
    langs = client.get_supported_languages()
    assert "en" in langs
    assert "hi" in langs
    assert "ta" in langs
    assert "te" in langs
    assert "bn" in langs
    assert langs["hi"]["native"] == "हिन्दी"
    assert langs["ta"]["native"] == "தமிழ்"


def test_bhashini_client_configuration():
    client = BhashiniClient(
        user_id="test-user",
        api_key="test-key",
        inference_key="test-infer",
    )
    assert client.is_configured is True
    assert client.user_id == "test-user"
    assert client.api_key == "test-key"
    assert client.inference_key == "test-infer"

    unconfigured = BhashiniClient(user_id="", api_key="", inference_key="")
    assert unconfigured.is_configured is False


def test_bhashini_translate_same_language():
    client = BhashiniClient()
    assert client.translate("Hello World", "en", "en") == "Hello World"
    assert client.translate("", "en", "hi") == ""


def test_bhashini_translate_mocked():
    client = BhashiniClient(
        user_id="dummy-user",
        api_key="dummy-key",
        inference_key="dummy-infer",
    )

    pipeline_mock_response = json.dumps({
        "pipelineInferenceAPIEndPoint": {
            "callbackUrl": "https://dhruva-api.bhashini.gov.in/services/inference/pipeline",
            "inferenceApiKey": {"name": "Authorization", "value": "dummy-infer"},
        },
        "pipelineResponseConfig": [
            {
                "taskType": "translation",
                "config": [{"serviceId": "ai4bharat/indictrans-v2-all-gpu--t4"}],
            }
        ],
    }).encode("utf-8")

    infer_mock_response = json.dumps({
        "pipelineResponse": [
            {
                "taskType": "translation",
                "output": [
                    {
                        "source": "Intellectual Property",
                        "target": "बौद्धिक संपदा",
                    }
                ],
            }
        ]
    }).encode("utf-8")

    mock_resp1 = MagicMock()
    mock_resp1.read.return_value = pipeline_mock_response
    mock_resp1.__enter__.return_value = mock_resp1

    mock_resp2 = MagicMock()
    mock_resp2.read.return_value = infer_mock_response
    mock_resp2.__enter__.return_value = mock_resp2

    with patch("urllib.request.urlopen", side_effect=[mock_resp1, mock_resp2]):
        translated = client.translate("Intellectual Property", source_lang="en", target_lang="hi")
        assert translated == "बौद्धिक संपदा"


def test_bhashini_api_endpoints():
    test_client = TestClient(app)

    # 1. Test languages endpoint
    resp = test_client.get("/api/bhashini/languages")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"
    assert "hi" in data["languages"]
    assert "Digital India Bhashini Division" in data["provider"]

    # 2. Test status endpoint
    resp = test_client.get("/api/bhashini/status")
    assert resp.status_code == 200
    data = resp.json()
    assert "mission" in data
    assert "National Language Translation Mission" in data["mission"]

    # 3. Test translate endpoint with mocked client
    with patch.object(BhashiniClient, "translate", return_value="परीक्षण अनुवाद"):
        resp = test_client.post(
            "/api/bhashini/translate",
            json={
                "text": "Test translation",
                "source_language": "en",
                "target_language": "hi",
            },
        )
        assert resp.status_code == 200
        data = resp.json()
        assert data["status"] == "ok"
        assert data["translated_text"] == "परीक्षण अनुवाद"
        assert data["provider"] == "bhashini"

def test_all_22_scheduled_languages():
    """Verify all 22 Eighth Schedule official Indian languages plus English are supported."""
    scheduled_22 = [
        "as", "bn", "brx", "doi", "gom", "gu", "hi", "kn", "ks", "mai",
        "ml", "mni", "mr", "ne", "or", "pa", "sa", "sat", "sd", "ta", "te", "ur",
    ]
    # Total 23 languages (22 scheduled + English)
    assert len(SUPPORTED_LANGUAGES) >= 23
    assert "en" in SUPPORTED_LANGUAGES
    assert SUPPORTED_LANGUAGES["en"]["name"] == "English"
    assert SUPPORTED_LANGUAGES["en"]["script"] == "Latn"

    for code in scheduled_22:
        assert code in SUPPORTED_LANGUAGES, f"Missing scheduled language: {code}"
        meta = SUPPORTED_LANGUAGES[code]
        assert "name" in meta and len(meta["name"]) > 0
        assert "native" in meta and len(meta["native"]) > 0
        assert "script" in meta and len(meta["script"]) > 0

    # Verify specific scripts
    assert SUPPORTED_LANGUAGES["hi"]["script"] == "Deva"
    assert SUPPORTED_LANGUAGES["ta"]["script"] == "Taml"
    assert SUPPORTED_LANGUAGES["te"]["script"] == "Telu"
    assert SUPPORTED_LANGUAGES["bn"]["script"] == "Beng"
    assert SUPPORTED_LANGUAGES["pa"]["script"] == "Guru"
    assert SUPPORTED_LANGUAGES["ur"]["script"] == "Arab"
    assert SUPPORTED_LANGUAGES["sat"]["script"] == "Olck"


def test_bhashini_ui_bundle_endpoint(tmp_path):
    """Test /api/bhashini/ui-bundle for en, hi, and mocked Indic language with disk caching."""
    test_client = TestClient(app)

    # 1. Test default parameter (defaults to "en")
    resp_def = test_client.get("/api/bhashini/ui-bundle")
    assert resp_def.status_code == 200
    data_def = resp_def.json()
    assert data_def["status"] == "ok"
    assert data_def["language"] == "en"
    assert data_def["bundle"]["navChat"] == "Chat Assistant"

    # 2. Test explicit "en"
    resp_en = test_client.get("/api/bhashini/ui-bundle?lang=en")
    assert resp_en.status_code == 200
    data_en = resp_en.json()
    assert data_en["status"] == "ok"
    assert data_en["language"] == "en"
    assert isinstance(data_en["bundle"], dict)
    assert data_en["bundle"]["navChat"] == "Chat Assistant"
    assert data_en["bundle"]["brandSub"] == "AI Assistant for Ayurvedic IP & Regulatory Guidance"

    # 3. Test explicit "hi"
    resp_hi = test_client.get("/api/bhashini/ui-bundle?lang=hi")
    assert resp_hi.status_code == 200
    data_hi = resp_hi.json()
    assert data_hi["status"] == "ok"
    assert data_hi["language"] == "hi"
    assert isinstance(data_hi["bundle"], dict)
    assert data_hi["bundle"]["navChat"] == "चैट सहायक"
    assert data_hi["bundle"]["brandSub"] == "आयुर्वेदिक IP एवं नियामक मार्गदर्शन हेतु AI सहायक"

    # 4. Test mocked Indic language (e.g. Tamil 'ta') with batch translation & disk caching
    def mock_translate_batch(texts, source_lang="en", target_lang="ta"):
        return [f"[ta_{t}]" for t in texts]

    with patch("ipsakti.core.bhashini.I18N_CACHE_DIR", tmp_path):
        with patch.object(BhashiniClient, "translate_batch", side_effect=mock_translate_batch):
            resp_ta = test_client.get("/api/bhashini/ui-bundle?lang=ta")
            assert resp_ta.status_code == 200
            data_ta = resp_ta.json()
            assert data_ta["status"] == "ok"
            assert data_ta["language"] == "ta"
            assert isinstance(data_ta["bundle"], dict)
            assert data_ta["bundle"]["navChat"] == "[ta_Chat Assistant]"

            # Check that it saved to the local disk cache
            cache_file = tmp_path / "ta.json"
            assert cache_file.is_file()

            # Second request should read directly from disk cache without calling translate_batch
            with patch.object(
                BhashiniClient,
                "translate_batch",
                side_effect=RuntimeError("translate_batch should not be called when cached!"),
            ):
                resp_ta_cached = test_client.get("/api/bhashini/ui-bundle?lang=ta")
                assert resp_ta_cached.status_code == 200
                data_cached = resp_ta_cached.json()
                assert data_cached["bundle"]["navChat"] == "[ta_Chat Assistant]"


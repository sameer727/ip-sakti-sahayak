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

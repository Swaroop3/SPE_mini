"""Integration tests for the FastAPI calculator service."""

from __future__ import annotations

from fastapi.testclient import TestClient

from spe_calculator.api import app

client = TestClient(app)


def test_root_endpoint() -> None:
    response = client.get("/")
    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"


def test_square_root_endpoint() -> None:
    response = client.get("/sqrt", params={"value": 16})
    assert response.status_code == 200
    assert response.json()["result"] == 4


def test_factorial_endpoint() -> None:
    response = client.get("/factorial", params={"value": 5})
    assert response.status_code == 200
    assert response.json()["result"] == 120


def test_natural_log_endpoint() -> None:
    response = client.get("/ln", params={"value": 1})
    assert response.status_code == 200
    assert response.json()["result"] == 0


def test_power_endpoint() -> None:
    response = client.get("/power", params={"base": 2, "exponent": 3})
    assert response.status_code == 200
    assert response.json()["result"] == 8


def test_invalid_request_returns_400() -> None:
    response = client.get("/sqrt", params={"value": -1})
    assert response.status_code == 400
    assert "undefined" in response.json()["detail"]


from fastapi.testclient import TestClient

from api.main import app


# Create a test client for our FastAPI application
client = TestClient(app)


def test_home_endpoint():
    """Check whether the API homepage works."""

    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_ask_endpoint():
    """Check whether the API accepts a customer question."""

    response = client.post(
        "/ask",
        json={"question": "What are your business hours?"}
    )

    assert response.status_code == 200
    assert "answer" in response.json()
    assert response.json()["question"] == "What are your business hours?"


def test_ask_endpoint_with_empty_question():
    """Check whether the API rejects an empty request body."""

    response = client.post(
        "/ask",
        json={}
    )

    assert response.status_code == 422

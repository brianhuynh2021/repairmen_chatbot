from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_chat_endpoint():
    payload = {"message": "Hello"}
    response = client.post("/chat", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert "reply" in data
    assert isinstance(data["reply"], str)

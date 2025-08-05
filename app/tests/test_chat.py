from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def chat_endpoint():
    payload = {"message": "Hello"}
    response = client.post("/chat", json=payload)
    
    assert response.status_code == 200
    assert "reply" in response.json()
    assert isinstance(response.json()["reply"], str)
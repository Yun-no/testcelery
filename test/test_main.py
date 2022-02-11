from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_main():
    response = client.get("/api/v1/bring/")
    assert response.status_code == 200
    assert response.json() == {"test_bring": "test"}


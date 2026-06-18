from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200

def test_predict():
    payload = {
        "recency": 30,
        "frequency": 5,
        "monetary": 1000,
        "ticket_count": 1,
        "return_rate": 0.1,
        "sessions_30d": 10
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200

def test_batch_predict():
    payload = {
        "customers": [
            {
                "recency": 30,
                "frequency": 5,
                "monetary": 1000,
                "ticket_count": 1,
                "return_rate": 0.1,
                "sessions_30d": 10
            }
        ]
    }

    response = client.post("/batch_predict", json=payload)

    assert response.status_code == 200

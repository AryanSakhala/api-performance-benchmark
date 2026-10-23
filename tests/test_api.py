from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    assert client.get("/health").json() == {"status": "ok"}


def test_ready():
    assert client.get("/ready").json()["status"] == "ready"


def test_compute_known_value():
    r = client.get("/compute/10")
    assert r.status_code == 200
    expected = 0
    for i in range(10):
        expected = (expected + i * 7) % 1_000_003
    assert r.json() == {"iterations": 10, "result": expected}


def test_compute_rejects_out_of_range():
    assert client.get("/compute/0").status_code == 422
    assert client.get("/compute/1000001").status_code == 422


def test_headers():
    r = client.get("/health", headers={"x-request-id": "abc"})
    assert r.headers["x-request-id"] == "abc"
    assert "x-process-time-ms" in r.headers

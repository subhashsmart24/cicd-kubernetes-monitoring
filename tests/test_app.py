from app.app import app


def test_home_endpoint():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200

    data = response.get_json()
    assert data["application"] == "DevOps CI/CD Monitoring Demo"
    assert data["status"] == "running"


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}


def test_metrics_endpoint():
    client = app.test_client()
    response = client.get("/metrics")

    assert response.status_code == 200
    assert b"app_http_requests_total" in response.data
    assert b"app_http_request_duration_seconds" in response.data
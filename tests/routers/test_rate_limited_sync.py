import pytest
from src.core.rate_limiter import limiter

@pytest.fixture(autouse=True)
def clean_rate_limiter():
    # Clean the rate limiter memory before each test
    limiter.reset()

def test_hello_endpoint_rate_limit(client):
    # Test successful requests within limit
    for _ in range(5):
        response = client.get("/sync/rate-limited/hello")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello from a synchronous endpoint!"}

    # Test rate limit exceeded
    response = client.get("/sync/rate-limited/hello")
    assert response.status_code == 429  # Too Many Requests
    assert "Rate limit exceeded" in response.text  # More flexible substring match

def test_hello_with_id_endpoint_rate_limit(client):
    # Test successful requests within limit
    for i in range(10):
        response = client.get(f"/sync/rate-limited/hello/999")
        assert response.status_code == 200
        assert response.json() == {"message": f"Hello from a synchronous endpoint! 999"}

    # Test rate limit exceeded
    response = client.get("/sync/rate-limited/hello/999")
    assert response.status_code == 429
    assert "Rate limit exceeded" in response.text

def test_burst_limit_endpoint(client):
    # Test the 5/minute limit
    for _ in range(5):
        response = client.get("/sync/rate-limited/burst")
        assert response.status_code == 200
        assert response.json() == {"message": "Testing burst rate limiting"}

    # Test rate limit exceeded for minute limit
    response = client.get("/sync/rate-limited/burst")
    assert response.status_code == 429
    assert "Rate limit exceeded" in response.text

def test_slow_endpoint_rate_limit(client):
    # Test successful requests within limit
    for _ in range(3):
        response = client.get("/sync/rate-limited/slow")
        assert response.status_code == 200
        assert response.json() == {"message": "This is a slow endpoint"}

    # Test rate limit exceeded
    response = client.get("/sync/rate-limited/slow")
    assert response.status_code == 429
    assert "Rate limit exceeded" in response.text
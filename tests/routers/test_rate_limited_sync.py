import time

def test_hello_endpoint_rate_limit(client):
    # Test successful requests within limit
    for _ in range(5):
        response = client.get("/sync/rate-limited/hello")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello from a synchronous endpoint!"}

    # Test rate limit exceeded
    response = client.get("/sync/rate-limited/hello")
    assert response.status_code == 429  # Too Many Requests
    assert "Request limit exceeded" in response.text

def test_hello_with_id_endpoint_rate_limit(client):
    # Test successful requests within limit
    for i in range(10):
        response = client.get(f"/sync/rate-limited/hello/{i}")
        assert response.status_code == 200
        assert response.json() == {"message": f"Hello from a synchronous endpoint! {i}"}

    # Test rate limit exceeded
    response = client.get("/sync/rate-limited/hello/999")
    assert response.status_code == 429
    assert "Request limit exceeded" in response.text

def test_burst_limit_endpoint(client):
    # Test the 5/minute limit
    for _ in range(5):
        response = client.get("/sync/rate-limited/burst")
        assert response.status_code == 200
        assert response.json() == {"message": "Testing burst rate limiting"}

    # Test rate limit exceeded for minute limit
    response = client.get("/sync/rate-limited/burst")
    assert response.status_code == 429
    assert "Request limit exceeded" in response.text

def test_slow_endpoint_rate_limit(client):
    # Test successful requests within limit
    for _ in range(3):
        response = client.get("/sync/rate-limited/slow")
        assert response.status_code == 200
        assert response.json() == {"message": "This is a slow endpoint"}

    # Test rate limit exceeded
    response = client.get("/sync/rate-limited/slow")
    assert response.status_code == 429
    assert "Request limit exceeded" in response.text

def test_rate_limit_reset(client):
    """Test that rate limits reset after waiting"""
    # Use up the rate limit
    for _ in range(5):
        client.get("/sync/rate-limited/hello")

    # Verify we're rate limited
    response = client.get("/sync/rate-limited/hello")
    assert response.status_code == 429

    # Wait for 60 seconds (rate limit to reset)
    time.sleep(60)

    # Verify we can make requests again
    response = client.get("/sync/rate-limited/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from a synchronous endpoint!"} 
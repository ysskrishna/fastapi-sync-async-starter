import pytest
from src.core.rate_limiter import limiter

@pytest.fixture(autouse=True)
def clean_rate_limiter():
    # Clean the rate limiter memory before each test
    limiter.reset()

@pytest.mark.asyncio
async def test_hello_endpoint_rate_limit(async_client):
    # Test successful requests within limit
    for _ in range(5):
        response = await async_client.get("/async/rate-limited/hello")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello from an asynchronous endpoint!"}

    # Test rate limit exceeded
    response = await async_client.get("/async/rate-limited/hello")
    assert response.status_code == 429
    assert "Rate limit exceeded" in response.text

@pytest.mark.asyncio
async def test_hello_with_id_endpoint_rate_limit(async_client):
    # Test successful requests within limit
    for i in range(10):
        response = await async_client.get(f"/async/rate-limited/hello/{i}")
        assert response.status_code == 200
        assert response.json() == {"message": f"Hello from an asynchronous endpoint! {i}"}

    # Test rate limit exceeded
    response = await async_client.get("/async/rate-limited/hello/999")
    assert response.status_code == 429
    assert "Rate limit exceeded" in response.text

@pytest.mark.asyncio
async def test_burst_limit_endpoint(async_client):
    # Test the 5/minute limit
    for _ in range(5):
        response = await async_client.get("/async/rate-limited/burst")
        assert response.status_code == 200
        assert response.json() == {"message": "Testing burst rate limiting"}

    # Test rate limit exceeded for minute limit
    response = await async_client.get("/async/rate-limited/burst")
    assert response.status_code == 429
    assert "Rate limit exceeded" in response.text

@pytest.mark.asyncio
async def test_slow_endpoint_rate_limit(async_client):
    # Test successful requests within limit
    for _ in range(3):
        response = await async_client.get("/async/rate-limited/slow")
        assert response.status_code == 200
        assert response.json() == {"message": "This is a slow endpoint"}

    # Test rate limit exceeded
    response = await async_client.get("/async/rate-limited/slow")
    assert response.status_code == 429
    assert "Rate limit exceeded" in response.text 
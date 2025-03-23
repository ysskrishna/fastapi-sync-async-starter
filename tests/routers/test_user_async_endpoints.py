import pytest
from src.models import models


@pytest.mark.asyncio
async def test_create_user_async(async_client):
    response = await async_client.post(
        "/async/users/",
        json={"email": "test_async@example.com", "name": "testuser_async"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test_async@example.com"
    assert data["name"] == "testuser_async"
    assert "user_id" in data


@pytest.mark.asyncio
async def test_read_users_async(async_client, async_db_session):
    # Create test users
    user1 = models.User(email="async_user1@example.com", name="async_user1")
    user2 = models.User(email="async_user2@example.com", name="async_user2")
    async_db_session.add_all([user1, user2])
    await async_db_session.commit()


    response = await async_client.get("/async/users/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["email"] == "async_user1@example.com"
    assert data[1]["email"] == "async_user2@example.com"
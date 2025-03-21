from src.models import models


def test_create_user(client):
    response = client.post(
        "/sync/users/",
        json={"email": "test@example.com", "name": "testuser"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"
    assert data["name"] == "testuser"
    assert "user_id" in data


def test_read_users(client, db_session):
    # Create test users
    user1 = models.User(email="user1@example.com", name="user1")
    user2 = models.User(email="user2@example.com", name="user2")
    db_session.add_all([user1, user2])
    db_session.commit()


    response = client.get("/sync/users/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["email"] == "user1@example.com"
    assert data[1]["email"] == "user2@example.com"

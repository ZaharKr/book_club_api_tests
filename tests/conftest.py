import uuid

import pytest
import requests

from helpers import register_user

BASE_URL = "https://book-club.qa.guru/api/v1"


@pytest.fixture
def unique_user():
    uid = uuid.uuid4().hex[:8]
    return {
        "username": f"zk_user_{uid}",
        "password": "TestPassword123",
    }


@pytest.fixture
def registered_user(unique_user):
    response = register_user(unique_user)
    assert response.status_code == 201, response.text
    return unique_user


@pytest.fixture
def api_client():
    session = requests.Session()
    session.headers.update({"Accept": "application/json"})
    return session


@pytest.fixture
def auth_client(registered_user):
    session = requests.Session()
    session.headers.update({"Accept": "application/json"})

    response = session.post(
        f"{BASE_URL}/auth/token/",
        json={
            "username": registered_user["username"],
            "password": registered_user["password"],
        },
    )
    assert response.status_code == 200, response.text
    access = response.json()["access"]
    session.headers.update({"Authorization": f"Bearer {access}"})
    return session


@pytest.fixture
def club_data():
    uid = uuid.uuid4().hex[:8]
    return {
        "bookTitle": f"ZK Test Book {uid}",
        "bookAuthors": "Test Author",
        "publicationYear": 2020,
        "description": "Test club description",
        "telegramChatLink": "https://t.me/test",
    }


@pytest.fixture
def created_club(auth_client, club_data):
    response = auth_client.post(f"{BASE_URL}/clubs/", json=club_data)
    assert response.status_code == 201, response.text
    club = response.json()

    yield club

    auth_client.delete(f"{BASE_URL}/clubs/{club['id']}/")

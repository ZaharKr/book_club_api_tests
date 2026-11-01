import requests
from jsonschema import validate

from schemas.clubs import CLUBS_LIST_SCHEMA

BASE_URL = "https://book-club.qa.guru/api/v1/clubs/"


def test_get_clubs_returns_200_and_results():
    response = requests.get(BASE_URL)

    assert response.status_code == 200
    body = response.json()
    assert isinstance(body["results"], list)
    assert body["count"] > 0
    assert body["results"], "Список клубов пуст"


def test_get_clubs_matches_json_schema():
    response = requests.get(BASE_URL)

    assert response.status_code == 200
    validate(instance=response.json(), schema=CLUBS_LIST_SCHEMA)


def test_get_clubs_first_item_has_book_data():
    response = requests.get(BASE_URL)

    assert response.status_code == 200
    club = response.json()["results"][0]

    assert club["id"] > 0
    assert club["bookTitle"].strip()
    assert club["bookAuthors"].strip()
    assert isinstance(club["publicationYear"], int) or club["publicationYear"] is None
    assert isinstance(club["members"], list)


def test_search_clubs_by_existing_title():
    list_response = requests.get(BASE_URL)
    assert list_response.status_code == 200

    book_title = list_response.json()["results"][0]["bookTitle"]
    search_response = requests.get(BASE_URL, params={"search": book_title})

    assert search_response.status_code == 200
    body = search_response.json()
    assert body["count"] >= 1
    assert body["results"]
    assert book_title in body["results"][0]["bookTitle"]


def test_get_clubs_pagination_page_size():
    response = requests.get(BASE_URL, params={"page": 1, "page_size": 2})

    assert response.status_code == 200
    body = response.json()
    assert body["count"] >= 2
    assert len(body["results"]) == 2
    validate(instance=body, schema=CLUBS_LIST_SCHEMA)

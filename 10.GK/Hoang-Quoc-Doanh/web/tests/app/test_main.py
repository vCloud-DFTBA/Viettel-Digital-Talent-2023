from fastapi.testclient import TestClient
from main import *

client = TestClient(app)


def test_get_all():
    response = client.get("/vdt-cloud/attendees")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_attendee():
    response = client.get("/vdt-cloud/attendees/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_get_attendee_not_found():
    response = client.get("/vdt-cloud/attendees/1000")
    assert response.json() == [{"error": "Attendee not found"}, 404]


def test_add_attendee():
    response = client.post(
        "/vdt-cloud/attendees",
        json={
            "id": 1000,
            "name": "Test User 1000",
            "username": "testuser1000",
            "birthyear": "1000",
            "gender": "unisex",
            "university": "Hardvard",
            "major": "Computer Science",
        },
    )
    assert response.status_code == 200


def test_add_attendee_invalid():
    response = client.post(
        "/vdt-cloud/attendees",
        json={
            "id": 1001,
            "name": "Test User",
            "username": "testuser",
            "invalid": "invalid",
        },
    )
    assert response.status_code == 422


def test_add_attendee_invalid_id():
    response = client.post(
        "/vdt-cloud/attendees",
        json={
            "id": "invalid",
            "name": "Test User",
            "username": "testuser",
            "birthyear": "1000",
            "gender": "unisex",
            "university": "Hardvard",
            "major": "Computer Science",
        },
    )
    assert response.status_code == 422


def test_add_attendee_existed_username():
    response = client.post(
        "/vdt-cloud/attendees",
        json={
            "id": 1002,
            "name": "Test User 1002",
            "username": "lamlt",
            "birthyear": "1000",
            "gender": "unisex",
            "university": "Hardvard",
            "major": "Computer Science",
        },
    )
    assert response.json() == [{"error": "Username already exists"}, 400]


def test_add_attendee_existed_id():
    response = client.post(
        "/vdt-cloud/attendees",
        json={
            "id": 1,
            "name": "Test User 1003",
            "username": "testuser 1003",
            "birthyear": "1000",
            "gender": "unisex",
            "university": "Hardvard",
            "major": "Computer Science",
        },
    )
    assert response.json() == [{"error": "Id already exists"}, 400]


def test_update_attendee():
    response = client.put(
        "/vdt-cloud/attendees/lamlt",
        json={
            "id": 1004,
            "name": "Test User 1004",
            "username": "testuser1004",
            "birthyear": "1000",
            "gender": "unisex",
            "university": "Hardvard",
            "major": "Computer Science",
        },
    )
    assert response.status_code == 200


def test_update_attendee_invalid():
    response = client.put(
        "/vdt-cloud/attendees/sonbm",
        json={
            "id": 1005,
            "name": "Test User 1005",
            "username": "testuser1005",
            "invalid": "invalid",
        },
    )
    assert response.status_code == 422


def test_update_attendee_existed_username():
    response = client.put(
        "/vdt-cloud/attendees/hiepdd",
        json={
            "id": 1006,
            "name": "Test User 1006",
            "username": "tuda",
            "birthyear": "1000",
            "gender": "unisex",
            "university": "Hardvard",
            "major": "Computer Science",
        },
    )
    assert response.json() == [{"error": "New username already exists"}, 400]


def test_update_attendee_existed_id():
    response = client.put(
        "/vdt-cloud/attendees/hiepdd",
        json={
            "id": 1,
            "name": "Test User 1007",
            "username": "testuser1007",
            "birthyear": "1000",
            "gender": "unisex",
            "university": "Hardvard",
            "major": "Computer Science",
        },
    )
    assert response.json() == [{"error": "New id already exists"}, 400]


def test_update_attendee_not_found():
    response = client.put(
        "/vdt-cloud/attendees/noname",
        json={
            "id": 1008,
            "name": "Test User 1008",
            "username": "testuser1008",
            "birthyear": "1000",
            "gender": "unisex",
            "university": "Hardvard",
            "major": "Computer Science",
        },
    )
    assert response.json() == [{"error": "Username not found"}, 404]


def test_patch_attendee():
    response = client.patch(
        "/vdt-cloud/attendees/lailp",
        json={
            "id": 1009,
            "name": "Test User 1009",
            "username": "testuser1009",
            "birthyear": "1000",
            "gender": "unisex",
            "university": "Hardvard",
            "major": "Computer Science",
        },
    )
    assert response.status_code == 200


def test_delete_attendee():
    response = client.delete("/vdt-cloud/attendees/chienlv")
    assert response.status_code == 200

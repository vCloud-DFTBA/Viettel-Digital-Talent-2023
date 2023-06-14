from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
import sys

sys.path.insert(0, "./")
from main import app

client = TestClient(app)


def test_add_user_info():
    response = client.post(
        "/add-user",
        json={
            "name": "test",
            "program": "test",
            "year": "test",
            "sex": "test",
            "avatar": "",
            "title": "test",
            "university": "test",
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "name": "test",
        "program": "test",
        "year": "test",
        "sex": "test",
        "avatar": "",
        "title": "test",
        "university": "test",
    }


def test_get_user_info():
    response = client.get("/user/test")
    assert response.status_code == 200
    assert response.json() == {
        "name": "test",
        "program": "test",
        "year": "test",
        "sex": "test",
        "avatar": "",
        "title": "test",
        "university": "test",
    }


def test_delete_user_info():
    response = client.post("/delete-user", json={"user": "test"})
    assert response.status_code == 200
    assert response.json() == {"status": True}


def test_update_user_info():
    response = client.post(
        "/update-user",
        json={
            "name": "test",
            "program": "updated_program",
            "year": "updated_year",
            "sex": "updated_sex",
            "avatar": "",
            "title": "updated_title",
            "university": "updated_university",
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "name": "test",
        "program": "updated_program",
        "year": "updated_year",
        "sex": "updated_sex",
        "avatar": "",
        "title": "updated_title",
        "university": "updated_university",
    }


def test_get_all_user():
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json() == {
        "users": [
            {
                "name": "test",
                "program": "updated_program",
                "year": "updated_year",
                "sex": "updated_sex",
                "avatar": "",
                "university": "updated_university",
                "title": "updated_title",
            }
        ]
    }


def test_image_endpoint():
    response = client.get("/media/")
    assert response.status_code == 404

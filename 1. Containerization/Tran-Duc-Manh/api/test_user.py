from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from core.config import logger
import sys
from main import app

def test_add_user_info():
    response = client.post(
        "/api/v1/add-user",
        data={
            "name": "test",
            "program": "Cloud",
            "year": 2022,
            "sex": "Nam",
            "avatar": "",
            "title": "test",
            "university": "test",
        },
    )
    assert response.status_code == 200
    assert response.json() == {
            "name": "test",
            "program": "Cloud",
            "year": 2022,
            "sex": "Nam",
            "avatar": "",
            "title": "test",
            "university": "test",
    }
    logger.info("Pass test add user")



def test_get_user_info():
    response = client.get("api/v1/user/test")
    assert response.status_code == 200
    assert response.json() == {
            "name": "test",
            "program": "Cloud",
            "year": 2022,
            "sex": "Nam",
            "avatar": "",
            "title": "test",
            "university": "test",
    }
    logger.info("Pass test get single user info")


def test_delete_user_info():
    response = client.post("/api/v1/delete-user", params={"user": "test"})
    assert response.status_code == 200
    assert response.json() == {"status": True}
    logger.info("Pass delete user")


def test_update_user_info():
    response = client.post(
        "/api/v1/update-user",
        data={
            "name": "test",
            "program": "Data science and AI",
            "year": 2022,
            "sex": "Nữ",
            "title": "Khoa học máy tính",
            "university": "Bách khoa Hà Nội",
        },
    )
    assert response.status_code == 200
    assert response.json() == {
            "name": "test",
            "program": "Data science and AI",
            "year": 2022,
            "sex": "Nữ",
            "avatar":"",
            "title": "Khoa học máy tính",
            "university": "Bách khoa Hà Nội",
        }
    logger.info("Pass update user")


def test_get_all_user():
    response = client.get("/api/v1/users")
    assert response.status_code == 200
    assert response.json().get("users") != None
    logger.info("Pass get all users")


def test_image_endpoint():
    response = client.get("/media/")
    assert response.status_code == 404


if __name__=="__main__":
    client = TestClient(app)
    test_delete_user_info()
    test_add_user_info()
    test_get_user_info()
    test_update_user_info()
    test_delete_user_info()
    test_get_all_user()

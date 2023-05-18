import requests
from flask_pymongo import MongoClient

ENDPOINT = "http://127.0.0.1:5000/"
client = MongoClient("mongodb://admin:Admin123@127.0.0.1:27017/", connectTimeoutMS=3000)
VDT_DB = client.VDTuser
db = VDT_DB.user

test_a = "sadsd"


def test_can_access_homepage():
    respone = requests.get(ENDPOINT)
    assert respone.status_code == 200


def test_can_call_endpoint():
    respone = requests.get(ENDPOINT + "members")
    assert respone.status_code == 200
    data = respone.json()
    print(data)


def test_user_api():
    students = db.find()
    for student in students:
        username = student["username"]
        respone = requests.get(ENDPOINT + f"members/{username}")
        assert respone.status_code == 200


def test_can_create_mem():
    payload = {
        "name": "Nguyen Thi Thuy Quynh",
        "year_of_birth": "2001",
        "university": "UET",
        "gender": "Female",
        "username": "quynhntt1",
        "major": "computer science",
    }
    respone = requests.post(ENDPOINT + "postdata", json=payload)

    assert respone.status_code == 200
    data = respone.json()
    print(data)


def test_can_del_mem():
    username = "quynhntt1"

    respone = requests.delete(ENDPOINT + f"delmember/{username}")
    assert respone.status_code == 200
    print(respone.status_code)


def test_can_update_mem():
    payload = {
        "name": "Nguyen Thi Thuy Quynh",
        "year_of_birth": "2002",
        "university": "UET",
        "gender": "Female",
        "username": "quynhntt",
        "major": "network and communication",
    }

    username = payload["username"]
    respone = requests.put(ENDPOINT + f"/updatemember/{username}", json=payload)
    assert respone.status_code == 200

    data = respone.json()
    print(data)

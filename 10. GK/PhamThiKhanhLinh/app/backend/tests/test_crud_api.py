from fastapi.testclient import TestClient
from http import client
import json

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

client = TestClient(app)

username = "somebody"

sample_data = {
    "name": "Anybody's Name",
    "username": username,
    "yearOfBirth": 2000,
    "sex": "Female",
    "university": "Maybe not UET university",
    "major": "Economy"
}

updated_data = {
    "name": "Somebody's Name with Bright Future",
    "username": username,
    "yearOfBirth": 2002,
    "sex": "Female",
    "university": "University of Engineering and Technology",
    "major": "Definitely Information Technology"
}

def test_add_attendee(mongo_mock):
    response = client.post(f"/newAttendee={username}", data=json.dumps(sample_data))
    assert response.status_code == 200
    assert response.json()["message"] == "Add new attendee successfully"
    assert response.json()["data"][0]["name"] == sample_data["name"]
    assert response.json()["data"][0]["username"] == sample_data["username"]
    assert response.json()["data"][0]["yearOfBirth"] == sample_data["yearOfBirth"]
    assert response.json()["data"][0]["sex"] == sample_data["sex"]
    assert response.json()["data"][0]["university"] == sample_data["university"]
    assert response.json()["data"][0]["major"] == sample_data["major"]

def test_get_attendee(mongo_mock):
    response = client.get(f"/{username}")
    assert response.status_code == 200
    assert response.json()["name"] == sample_data["name"]
    assert response.json()["username"] == sample_data["username"]
    assert response.json()["yearOfBirth"] == sample_data["yearOfBirth"]
    assert response.json()["sex"] == sample_data["sex"]
    assert response.json()["university"] == sample_data["university"]
    assert response.json()["major"] == sample_data["major"]

def test_get_attendee_list():
    response = client.get("/")
    assert response.status_code == 200

def test_update_attendee(mongo_mock):
    response = client.put(f"/editAttendee={username}", data=json.dumps(updated_data))
    assert response.status_code == 200
    assert response.json()["message"] == "Update attendee successfully"

def test_delete_employee(mongo_mock):
    response = client.delete(f"/deleteAttendee={username}")
    assert response.status_code == 200
    assert response.json()["message"] == "Delete attendee successfully"
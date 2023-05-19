import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.fixture(scope="module")
def student_data():
    return {
        "stt": "100",
        "name": "Le Minh",
        "username": "minhle",
        "year_of_birth": "2000",
        "gender": "male",
        "university": "ITMO",
        "major": "CS"
    }


def test_get_all():
    response = client.get("/api/v1/students")
    assert response.status_code == 200
    assert response.json() is not None

def test_post(student_data):
    response = client.post("/api/v1/students", json=student_data)
    assert response.status_code == 200
    response_data = response.json()
    del response_data['data']['id']
    expected_data = {
        "data": {
            "stt": 100,
            "name": "Le Minh",
            "username": "minhle",
            "year_of_birth": 2000,
            "gender": "male",
            "university": "ITMO",
            "major": "CS"
        },
        "code": 200,
        "message": "Student added successfully."
    }
    assert response_data == expected_data


def test_get_by_id(student_data):
    response1 = client.post("/api/v1/students", json=student_data)
    student_id = response1.json()['data']['id']
    response2 = client.get(f"/api/v1/students/{student_id}")
    assert response2.status_code == 200
    response2_data = response2.json()
    del response2_data['data']['_id']
    expected_data = {
        'data': {
            "stt": 100,
            "name": "Le Minh",
            "username": "minhle",
            "year_of_birth": 2000,
            "gender": "male",
            "university": "ITMO",
            "major": "CS"
        },
        'code': 200,
        'message': 'Student data retrieved successfully'
    }
    assert response2_data == expected_data

def test_update(student_data):
    response1 = client.post("/api/v1/students", json=student_data)
    student_id = response1.json()['data']['id']
    updated_data = {
        "stt": 100,
        "name": "Le Minh",
        "username": "minhle",
        "year_of_birth": 2000,
        "gender": "male",
        "university": "ITMO",
        "major": "CS"
    }
    response2 = client.put(f"/api/v1/students/{student_id}", json=updated_data)
    assert response2.status_code == 200
    expected_data = {
        "data": f"Student with ID: {student_id} name update is successful",
        "code": 200,
        "message": "Student name updated successfully"
    }
    assert response2.json() == expected_data

def test_delete(student_data):
    response1 = client.post("/api/v1/students", json=student_data)
    student_id = response1.json()['data']['id']
    response2 = client.delete(f"/api/v1/students/{student_id}")
    assert response2.status_code == 200
    expected_data = {
        "data": f"Student with ID: {student_id} removed",
        "code": 200,
        "message": "Student deleted successfully"
    }
    assert response2.json
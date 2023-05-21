from fastapi.testclient import TestClient
import logging
from main import app
logging.basicConfig(level=logging.DEBUG)

client = TestClient(app)

def test_post_student():
    logging.info("Start the post student test")
    response = client.post(
        "/api/v1/students",
        json={
            "stt": "0",
            "name": "Arthur Xiaomi",
            "username": "arthurx",
            "year_of_birth": "2000",
            "gender": "male",
            "university": "Birmingham",
            "major": "English Gangster"
        }
    )
    assert response.status_code == 200
    response_data = response.json()
    del response_data['data']['id']
    assert response_data == {
        "data": 
            {
            "stt": 0,
            "name": "Arthur Xiaomi",
            "username": "arthurx",
            "year_of_birth": 2000,
            "gender": "male",
            "university": "Birmingham",
            "major": "English Gangster"
            }
        ,
        "code": 200,
        "message": "Student added successfully."
    }
    logging.info("Pass the student post test")

def test_get_all_students():
    logging.info("Start the get all students test")
    response = client.get("/api/v1/students")
    assert response.status_code == 200
    assert response.json() != None
    logging.info("Pass the get all students test")

def test_get_student_by_id():
    logging.info("Start the get student by id test")
    response1 = client.post(
        "/api/v1/students",
        json={
            "stt": "0",
            "name": "Arthur Xiaomi",
            "username": "arthurx",
            "year_of_birth": "2000",
            "gender": "male",
            "university": "Birmingham",
            "major": "English Gangster"
        }
    )
    student_id = response1.json()['data']['id']
    response2 = client.get(f"/api/v1/students/{student_id}")
    assert response2.status_code == 200
    response2_data = response2.json()
    del response2_data['data']['_id']
    print(response2_data)
    assert response2_data == {
        'data': 
            {
            'stt': 0, 
            'name': 'Arthur Xiaomi', 
            'username': 'arthurx', 
            'year_of_birth': 2000, 
            'gender': 'male', 
            'university': 'Birmingham', 
            'major': 'English Gangster'
            },
        'code': 200, 
        'message': 'Student data retrieved successfully'
    }
    logging.info("Pass the get student by id test")

def test_update_student():
    logging.info("Start the update student test")
    response1 = client.post(
        "/api/v1/students",
        json={
            "stt": "0",
            "name": "Arthur Xiaomi",
            "username": "arthurx",
            "year_of_birth": "2000",
            "gender": "male",
            "university": "Birmingham",
            "major": "English Gangster"
        }
    )
    student_id = response1.json()['data']['id']
    response2 = client.put(f"/api/v1/students/{student_id}", json={
            "stt": "0",
            "name": "Thomas Xiaomi",
            "username": "thomasx",
            "year_of_birth": "2001",
            "gender": "male",
            "university": "Birmingham",
            "major": "English Gangster"
        })
    assert response2.status_code == 200
    assert response2.json() == {
        "data": f"Student with ID: {student_id} name update is successful",
        "code": 200,
        "message": "Student name updated successfully"
    }
    logging.info("Pass the update student test")

def test_delete_student():
    logging.info("Start the delete student test")
    response1 = client.post(
        "/api/v1/students",
        json={
            "stt": "0",
            "name": "Arthur Xiaomi",
            "username": "arthurx",
            "year_of_birth": "2000",
            "gender": "male",
            "university": "Birmingham",
            "major": "English Gangster"
        }
    )
    student_id = response1.json()['data']['id']
    response2 = client.delete(f"/api/v1/students/{student_id}")
    assert response2.status_code == 200
    assert response2.json() == {
        "data": f"Student with ID: {student_id} removed",
        "code": 200,
        "message": "Student deleted successfully"
    }
    logging.info("Pass the update student test")

if __name__=="__main__":
    test_post_student()
    test_get_all_students()
    test_get_student_by_id()
    test_update_student()
    test_delete_student()
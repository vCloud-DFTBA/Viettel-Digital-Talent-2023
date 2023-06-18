import pytest
import mongomock

@pytest.fixture()
def mongo_mock():
    client = mongomock.MongoClient()
    db = client.get_database("vdt-test")
    col = db.get_collection("attendees-test")
    emp_data = {
        "name": "Somebody's Name",
        "username": "namesb",
        "yearOfBirth": 2002,
        "sex": "Male",
        "university": "Any university",
        "major": "Not Information Technology"
    }

    col.insert_one(emp_data)

import pytest
import json
from mongomock import MongoClient

@pytest.fixture
def db():
    client = MongoClient()
    db = client.attendee
    with open('data/attendees.json') as f:
        data = json.load(f)
    db.attendees.insert_many(data)
    yield db
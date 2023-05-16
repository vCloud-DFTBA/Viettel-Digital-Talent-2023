from pymongo import MongoClient
import json

def create_db():
    client = MongoClient('mongodb://db:27017')
    client.drop_database('attendee')
    db = client.attendee
    if 'attendees' not in db.list_collection_names():
        with open('data/attendees.json') as f:
            data = json.load(f)
        db.attendees.insert_many(data)

    return db
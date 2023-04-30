import os
from flask import Flask
from pymongo import MongoClient
application = Flask(__name__)

MONGODB_DATABASE = os.environ.get("MONGODB_DATABASE")
MONGODB_HOSTNAME = os.environ.get("MONGODB_HOSTNAME")

client = MongoClient(f"{MONGODB_HOSTNAME}:27017")
db = client[MONGODB_DATABASE]
collection = db.attendees

@application.route("/profiles")
def profiles():
    attendees = []
    for attendee in collection.find():
        attendee.pop('_id', None)
        attendees.append(attendee)
    response = {
        "attendees": attendees
    }
    return response
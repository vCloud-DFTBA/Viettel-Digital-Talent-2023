import os
from flask import Flask, request
from pymongo import MongoClient
from bson import ObjectId, errors
application = Flask(__name__)

MONGODB_DATABASE = os.environ.get("MONGODB_DATABASE")
MONGODB_HOSTNAME = os.environ.get("MONGODB_HOSTNAME")
HOST_URL = os.environ.get("HOST_URL")

client = MongoClient(f"{MONGODB_HOSTNAME}:27017")
db = client[MONGODB_DATABASE]
collection = db.attendees

def is_valid(profile):
    print(profile)
    props = ['name','birth_year','gender','university','major']
    for prop in profile.keys():
        if prop not in props:
            return False
        
    if profile.get('name', '') == '':
        return False
    if collection.find_one({'name': profile['name']}):
        return False
    return True

@application.route("/api/profiles")
def profiles():
    attendees = []
    for attendee in collection.find():
        attendee['_id'] = str(attendee['_id'])
        attendees.append(attendee)
    response = {
        "ip": HOST_URL,
        "attendees": attendees
    }
    return response, 200
    
@application.route("/api/profile/create", methods=["POST"])
def create_profile():
    profile = {
        'name': request.form.get('name', ''),
        'birth_year': request.form.get('birth_year', ''),
        'gender': request.form.get('gender', ''),
        'university': request.form.get('university', ''),
        'major': request.form.get('major', ''),
    }

    if is_valid(profile):
        result = collection.insert_one(profile)
        return str(result.inserted_id) , 201

    return "not a valid profile", 400

@application.route("/api/profile/<id>", methods=["GET"])
def read_profile(id):
    try:
        attendee = collection.find_one({"_id": ObjectId(id)})
    except errors.InvalidId:
        return "attendee doesn't exist", 404

    attendee['_id'] = str(attendee['_id'])
    return attendee, 200
        

@application.route("/api/profile/<id>", methods=["PUT"])
def update_profile(id):
    updates = {
        'birth_year': request.form.get('birth_year', ''),
        'gender': request.form.get('gender', ''),
        'university': request.form.get('university', ''),
        'major': request.form.get('major', ''),
    }

    try:
        collection.find_one({"_id": ObjectId(id)})
    except errors.InvalidId:
        return "attendee doesn't exist", 404
    
    if updates:
        result = collection.update_one({'_id': ObjectId(id)}, {'$set': updates})
        return str(result.modified_count), 200


@application.route("/api/profile/<id>", methods=["DELETE"])
def delete_profile(id):
    try:
        collection.find_one({"_id": ObjectId(id)})
    except errors.InvalidId:
        return "attendee doesn't exist", 404
    
    result = collection.delete_one({'_id': ObjectId(id)})
    return str(result.deleted_count), 200
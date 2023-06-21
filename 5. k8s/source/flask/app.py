from flask import Flask, jsonify
from pymongo import MongoClient
import socket
import os

from init import init_database

def create_formatted_student(mentee):
    return {
        '_id': str(mentee['_id']),
        'full_name': mentee['full_name'],
        'birth_year': mentee['birth_year'],
        'gender': mentee['gender'],
        'university': mentee['university'],
        'major': mentee['major']
    }
app = Flask(__name__)

USER_NAME = os.environ.get("USER_NAME")
USER_PWD = os.environ.get("USER_PWD")
DB_SERVICE = "database"
MONGODB_DATABASE = "vdt2023"

uri = f'mongodb://{USER_NAME}:{USER_PWD}@{DB_SERVICE}:27017/'
client = MongoClient(uri)

db = client[f'{MONGODB_DATABASE}']
students_collection = db.attendees

@app.route('/')
def mentee_list():
    mentees = list(db.attendees.find({}))
    formatted_students = [create_formatted_student(mentee) for mentee in mentees]
    return jsonify(formatted_students)


if __name__ == '__main__':
    init_database('static/attendees.csv', students_collection)
    app.run(debug=True, use_debugger=False, use_reloader=False, host="0.0.0.0")

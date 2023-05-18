import json

from flask import Flask, jsonify, render_template, redirect, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://db:27017/")
db = client["internees"]


@app.route('/list')
def index():
    attendees = list(db.internees.find({}, {"_id": 0}))  # Exclude _id field
    api_json = []
    for attendee in attendees:
        api_json.append(attendee)
    return json.dumps(api_json, ensure_ascii=False).encode('utf-8')

@app.route("/addStudent", methods=['POST'])
def add_student():
    data = request.get_json()
    id = data["id"]
    name = data["name"]
    username = data['username']
    year = int(data["birth"])
    gender = data["sex"]
    school = data["university"]
    major = data["major"]
    db.internees.insert_one({
        'id': id,
        'name': name,
        'username' : username,
        'birth': year,
        'sex': gender,
        'university': school,
        'major': major
    })
    return jsonify({'message': 'Student added successfully'}), 201

@app.route('/deleteStudent/<int:id>', methods=['DELETE'])
def delete_student(id):
    id = str(id)
    db.internees.delete_one({'id': id})
    return jsonify({'message': 'Student deleted successfully'}), 200

@app.route('/view/<int:id>', methods=['GET'])
def view_student(id):
    id = str(id)
    student = db.internees.find_one({'id': id}, {"_id": 0})
    api_json = []
    api_json.append(student)
    return json.dumps(api_json, ensure_ascii=False).encode('utf-8')
    return jsonify({'message': 'Student not found'}), 404

@app.route('/updateStudent/<int:id>', methods=['POST'])
def update_student(id):
    id = str(id)
    student = db.internees.find_one({'id': id})
    if not student:
        return jsonify({'message': 'Student not found'}), 404

    data = request.get_json()
    name = data["name"]
    username = data['username']
    year = int(data["birth"])
    gender = data["sex"]
    school = data["university"]
    major = data["major"]

    db.internees.update_one(
        {'id': id},
        {"$set": {
            'name': name,
            'username' : username,
            'birth': year,
            'sex': gender,
            'university': school,
            'major': major
        }}
    )
    return jsonify({'message': 'Student updated successfully'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)
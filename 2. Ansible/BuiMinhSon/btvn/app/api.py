from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
CORS(app)

client = MongoClient('mongodb://mongodb:27017/')  # Thay đổi URI để kết nối với container MongoDB
db = client.test_database
collection = db.attendees  # Thay đổi tên collection

@app.route('/')
def VDT():
    return "Bui Minh Son - VDT" 

@app.route('/users')
def users():
    data = []
    for element in collection.find():
        item = {
            'id': str(element['_id']),
            'STT': element['STT'],
            'Name': element['Name'],
            'YearOfBirth': element['YearOfBirth'],
            'Sex': element['Sex'],
            'School': element['School'],
            'Major': element['Major']
        }
        data.append(item)

    return jsonify(data)

@app.route('/user', methods=['POST'])
def save_user():
    STT = request.json['STT']
    Name = request.json['Name']
    YearOfBirth = request.json['YearOfBirth']
    Sex = request.json['Sex']
    School = request.json['School']
    Major = request.json['Major']
    user = {
        'STT': STT,
        'Name': Name,
        'YearOfBirth': YearOfBirth,
        'Sex': Sex,
        'School': School,
        'Major': Major
    }
    collection.insert_one(user)

    return jsonify({'status': 'success'})

@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    result = collection.delete_one({'_id': ObjectId(id)})
    if result.deleted_count == 1:
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'fail'})
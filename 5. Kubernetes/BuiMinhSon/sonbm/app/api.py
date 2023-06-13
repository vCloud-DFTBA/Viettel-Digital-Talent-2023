from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId
import os
app = Flask(__name__)
CORS(app)

client = MongoClient(host=os.environ.get('MONGO_HOST'),  
                     username=os.environ.get('MONGO_USERNAME'), 
                     password=os.environ.get('MONGO_PASSWORD'), 
                     authSource='admin')

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
    Name = request.json['Name']
    YearOfBirth = request.json['YearOfBirth']
    Sex = request.json['Sex']
    School = request.json['School']
    Major = request.json['Major']
    user = {
       
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
    
@app.route('/user/<id>', methods=['GET'])
def get_user(id):
    user = collection.find_one({'_id': ObjectId(id)})
    if user:
        response = {
            'id': str(user['_id']),
            'Name': user['Name'],
            'YearOfBirth': user['YearOfBirth'],
            'Sex': user['Sex'],
            'School': user['School'],
            'Major': user['Major']
        }
        return jsonify(response)
    else:
        return jsonify({'status': 'fail', 'message': 'User not found'})
    
@app.route('/user/<id>', methods=['PUT'])
def update_user(id):
    user = collection.find_one({'_id': ObjectId(id)})
    if not user:
        return jsonify({'status': 'fail', 'message': 'User not found'})

    # Update user information
    user['Name'] = request.json.get('Name', user['Name'])
    user['YearOfBirth'] = request.json.get('YearOfBirth', user['YearOfBirth'])
    user['Sex'] = request.json.get('Sex', user['Sex'])
    user['School'] = request.json.get('School', user['School'])
    user['Major'] = request.json.get('Major', user['Major'])

    # Save updated user to database
    result = collection.replace_one({'_id': ObjectId(id)}, user)
    if result.modified_count == 1:
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'fail'})
    

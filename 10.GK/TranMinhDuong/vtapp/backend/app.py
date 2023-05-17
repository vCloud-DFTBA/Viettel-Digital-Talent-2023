from flask import Flask, jsonify, request
from pymongo import MongoClient
from flask_cors import CORS
import os

app = Flask(__name__)
cors = CORS(app)
# client = MongoClient(host='md_mongodb', port=27017, username='mongoAdmin', password='admin123', authSource='admin')

client = MongoClient(host=os.environ.get('MONGO_HOST'), 
                     port=int(os.environ.get('MONGO_PORT')), 
                     username=os.environ.get('MONGO_USERNAME'), 
                     password=os.environ.get('MONGO_PASSWORD'), 
                     authSource='admin')

db = client.vdt2023
currentCollection = db.attendees

@app.route('/whoami', methods = ['GET'])
def getHostName():
    return jsonify(os.environ.get('ANSIBLE_HOST'))

@app.route('/attendees', methods = ['GET'])
def getAllAttendees():
    attendeeList = list() 
    for i in currentCollection.find().sort("id"):
        attendeeList.append({'id':int(i['id']), 'name':i['name'], 'birthyear':i['birthyear'], 'gender':i['gender'],
                              'university':i['university'], 'major':i['major']})
    return jsonify(attendeeList)

@app.route('/attendee/<id>', methods = ['GET'])
def getAttendeeById(id):
    id = int(id)
    attendee = currentCollection.find_one({"id": id})
    if (attendee):
        return jsonify({'id':int(attendee['id']), 'name':attendee['name'], 'birthyear':attendee['birthyear'], 'gender':attendee['gender'],
                              'university':attendee['university'], 'major':attendee['major']})
    return jsonify({'message': 'Attendee Not Found'}), 404

@app.route('/add', methods = ['POST'])
def addAttendee():
    id = request.json['id']
    name = request.json['name']
    birthyear = request.json['birthyear']
    gender = request.json['gender']
    university = request.json['university']
    major = request.json['major']

    id = int(id)
    attendee = currentCollection.find_one({"id": id})
    # Check attendee exist
    if (attendee): 
        return jsonify({'message': 'Exist Attendee with same id'}), 400
    
    currentCollection.insert_one({'id': id, 'name': name, 'birthyear': birthyear, 
                                  'gender': gender, 'university': university, 'major': major})
    
    return jsonify({'message': 'Add successfully'}), 201

@app.route('/update/<id>', methods = ['PUT'])
def updateAttendee(id):
    id = int(id)
    # Check attendee exist
    attendee = currentCollection.find_one({'id' : id})
    if (attendee == None) :
        return jsonify({'message': 'Attendee Not Found'}), 400
    
    updatedId = request.json['id'] or attendee['id']
    updatedName = request.json['name'] or attendee['name']
    updatedBirthyear = request.json['birthyear'] or attendee['birthyear']
    updatedGender = request.json['gender'] or attendee['gender']
    updatedUniversity = request.json['university'] or attendee['university']
    updatedMajor = request.json['major'] or attendee['major']

    updateCount = currentCollection.update_one({'id' : id}, {"$set" : {'id': updatedId, 'name': updatedName, 'birthyear': updatedBirthyear, 'gender': updatedGender,
                                                'university': updatedUniversity, 'major': updatedMajor}}).modified_count
    # Check if modify success
    if (updateCount == 1) :
        return jsonify({'message': 'Edit successfully'})
    return jsonify({'message': 'No attendee updated'})

@app.route('/delete/<id>', methods = ['DELETE'])
def deleteAttendee(id):
    id = int(id)
    deleteCount = currentCollection.delete_one({'id': id}).deleted_count
    # Check if delete success
    if (deleteCount == 1):
        return jsonify({'message': 'Delete successfully'})
    return jsonify({'message': 'No attendee deleted'})

if __name__== '__main__':
    app.run(debug = True)
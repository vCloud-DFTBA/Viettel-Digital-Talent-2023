from flask import Flask, jsonify, request
from pymongo import MongoClient
from flask_cors import CORS
# ...

app = Flask(__name__)
cors = CORS(app)
client = MongoClient(host='md_mongodb', port=27017, username='mongoAdmin', password='admin123', authSource='admin')
db = client.vdt2023
currentCollection = db.attendees

@app.route('/attendees', methods = ['GET'])
def getAllAttendees():
    attendeeList = list() 
    for i in currentCollection.find().sort("id"):
        attendeeList.append({'id':int(i['id']), 'name':i['name'], 'birthyear':i['birthyear'], 'gender':i['gender'],
                              'university':i['university'], 'major':i['major']})
    return jsonify(attendeeList)

@app.route('/attendee/<id>', methods = ['GET'])
def getAttendeesById(id):
    id = int(id)
    attendee = currentCollection.find_one({"id": id})
    if (attendee):
        return jsonify({'id':int(attendee['id']), 'name':attendee['name'], 'birthyear':attendee['birthyear'], 'gender':attendee['gender'],
                              'university':attendee['university'], 'major':attendee['major']})
    return jsonify({'none': 'none'})

@app.route('/add', methods = ['POST'])
def addAttendee():
    id = request.json['id']
    name = request.json['name']
    birthyear = request.json['birthyear']
    gender = request.json['gender']
    university = request.json['university']
    major = request.json['major']
    currentCollection.insert_one({'id': int(id), 'name': name, 'birthyear': birthyear, 'gender': gender, 'university': university, 'major': major})
    return jsonify({'id': id, 'name': name, 'birthyear': birthyear, 'gender': gender, 'university': university, 'major': major})

@app.route('/update/<id>', methods = ['PUT'])
def updateAttendee(id):
    id = int(id)
    attendee = currentCollection.find_one({'id' : id})
    updatedId = request.json['id'] or attendee['id']
    updatedName = request.json['name'] or attendee['name']
    updatedBirthyear = request.json['birthyear'] or attendee['birthyear']
    updatedGender = request.json['gender'] or attendee['gender']
    updatedUniversity = request.json['university'] or attendee['university']
    updatedMajor = request.json['major'] or attendee['major']
    currentCollection.update_one({'id' : id}, {"$set" : {'id': updatedId, 'name': updatedName, 'birthyear': updatedBirthyear, 'gender': updatedGender,
                                                'university': updatedUniversity, 'major': updatedMajor}})
    return jsonify({'message': 'Edit successfully'})

@app.route('/delete/<id>', methods = ['DELETE'])
def deleteAttendee(id):
    id = int(id)
    currentCollection.delete_one({'id': id})
    return jsonify({'message': 'Delete successfully'})

if __name__== '__main__':
    app.run(debug = True)
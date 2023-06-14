from flask import Flask, jsonify, render_template, request, redirect, url_for
import pymongo
from pymongo import MongoClient
import os
import json

app = Flask(__name__)
client = MongoClient("mongodb://web_mongo:27017/")
db = client["internees"]

def insert_data(id = '', name= '', username= '', birth = '', sex = '', university = '', major = ''):
    db.internees.insert_one({'id':id, 'name': name, 'username': username , 'birth': birth, 'sex': sex , 'university': university, 'major': major})

def delete_data(id = ''):
    db.internees.delete_one({'id':id})

def update_data(id = '', name= '', username= '', birth = '', sex = '', university = '', major = ''):
    db.internees.update_one({'id': id}, {'$set': {'name': name, 'username': username , 'birth': birth, 'sex': sex , 'university': university, 'major': major}})


@app.route('/api/attendees', methods=['GET'])
def read():
    all_attendees = db.internees.find()

    api_json = []

    for attendee in all_attendees:
        api_json.append({key: value for key, value in attendee.items() if key != '_id'})

    return json.dumps(api_json, ensure_ascii=False).encode('utf-8')
        

@app.route('/api/create', methods=['POST'])
def creat_post():
    data = request.get_json()
    insert_data(
        data['id'], data['name'], data['username'], data['birth'], data['sex'], data['university'], data['major']
    )

    return jsonify(data)

    
@app.route('/api/update', methods=['POST'])
def update_post():
    data = request.get_json()
    update_data(
        data['id'], data['name'], data['username'], data['birth'], data['sex'], data['university'], data['major']
    )

    return jsonify(data)

@app.route('/api/delete/<int:id>')
def delete_post(id):

    id = str(id)   
    delete_data(id)
    return "Delete successfully"

@app.route('/api/read/<int:id>')
def read_post(id):

    id = str(id)
    students = []
    students.append(db.internees.find_one({"id": id}))

    api_json = []
    for attendee in students:
        api_json.append({key: value for key, value in attendee.items() if key != '_id'})
    return json.dumps(api_json, ensure_ascii=False).encode('utf-8')

if __name__=='__main__':
    app.run(host='0.0.0.0', port=9090, debug=True)

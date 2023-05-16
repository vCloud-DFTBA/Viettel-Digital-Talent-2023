from flask import Flask, jsonify, render_template, request, redirect, url_for
import pymongo
from pymongo import MongoClient
import os
import json
from dao import get_db, insert_data, delete_data, update_data

app = Flask(__name__)


@app.route('/api/attendees', methods=['GET'])
def read():
    db=""
    try:
        db = get_db()
        all_attendees = db.internees.find()

        api_json = []

        for attendee in all_attendees:
            api_json.append({k: v for k, v in attendee.items() if k != '_id'})

        return json.dumps(api_json, ensure_ascii=False).encode('utf-8')
        
    except:
        pass
    finally:
        if type(db)==MongoClient:
            db.close()


@app.route('/api/create', methods=['POST'])
def creat_post():
    try:
        data = request.get_json()
        insert_data(
            data['id'], data['name'], data['username'], data['birth'], data['sex'], data['university'], data['major']
        )

        return jsonify(data)
    except:
        return "Error!"
    

    
@app.route('/api/update', methods=['POST'])
def update_post():
    try:
        data = request.get_json()
        update_data(
            data['id'], data['name'], data['username'], data['birth'], data['sex'], data['university'], data['major']
        )

        return jsonify(data)
    except:
        return "Error!"

@app.route('/api/delete/<int:id>')
def delete_post(id):

    id = str(id)
    try:    
        if id != '29':
            delete_data(id)
        return "<h1 style='text-align:center; color: blue'>Delete succesfully. Reload the home page to see the differences!</h1>"
    except:
        return "Error!"

@app.route('/api/read/<int:id>')
def read_post(id):

    id = str(id)
    try:
        db = get_db()
        students = []
        students.append(db.internees.find_one({"id": id}))

        api_json = []
        for attendee in students:
            api_json.append({k: v for k, v in attendee.items() if k != '_id'})

        
        return json.dumps(api_json, ensure_ascii=False).encode('utf-8')
    
    except:
        return "Error!"

if __name__=='__main__':
    # app.run(host="0.0.0.0", port=5000)
    app.run(host='0.0.0.0', port=9090, debug=True)

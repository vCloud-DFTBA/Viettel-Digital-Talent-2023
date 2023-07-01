from flask import Flask, jsonify, redirect, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://mongodb:27017/')
db = client.test_database

@app.route('/')
def VDT():
    return "Bui Minh Son - VDT" 

@app.route('/users')
def users():
    collection = db.users.find()

    data = []
    for element in collection:
        item = {
            'id': str(element['_id']),
            'ho_ten': element['ho_ten'],
            'nam_sinh': element['nam_sinh'],
            'truong': element['truong']
        }
        data.append(item)

    return render_template('users.html', data=data)

@app.route('/user')
def add_user():
    return render_template('add_user.html')

@app.route('/user', methods=['POST'])
def save_user():
    ho_ten = request.form['ho_ten']
    nam_sinh = request.form['nam_sinh']
    truong = request.form['truong']
    user = {
        'ho_ten': ho_ten,
        'nam_sinh': nam_sinh,
        'truong': truong
    }
    db.users.insert_one(user)

    return render_template('add_user.html')
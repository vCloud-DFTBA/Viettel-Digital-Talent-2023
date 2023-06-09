from flask import Flask, jsonify, render_template, request
import pymongo
from pymongo import MongoClient
import os
import json
from dao import get_db, insert_data, delete_data, update_data

app = Flask(__name__)


@app.route('/')
def get_stored_animals():
    db=""
    try:
        db = get_db()

        # return render_template('index.html', value = db.internees.find())
        return render_template('home.html')
    except:
        pass
    finally:
        if type(db)==MongoClient:
            db.close()

@app.route('/read', methods=['GET'])
def read():
    db=""
    try:
        db = get_db()
        return render_template('index.html', value = db.internees.find())
    except:
        pass
    finally:
        if type(db)==MongoClient:
            db.close()

@app.route('/create', methods=['GET'])
def create():
    return render_template('create.html')

@app.route('/create', methods=['POST'])
def creat_post():
    id = request.form['id']
    name = request.form['name']
    sex = request.form['sex']
    birth = request.form['birth']
    university = request.form['university']
    major = request.form['major']
    username = request.form['username']

    insert_data(id, name, username, birth, sex, university, major)

    return render_template('home.html')
    

@app.route('/delete', methods=['GET'])
def delete():
    return render_template('delete.html')

@app.route('/delete', methods=['POST'])
def delete_post():
    id = request.form['id']
    delete_data(id)
    return render_template('home.html')


@app.route('/update', methods=['GET'])
def update():
    return render_template('update.html')

@app.route('/update', methods=['POST'])
def update_post():
    id = request.form['id']
    name = request.form['name']
    sex = request.form['sex']
    birth = request.form['birth']
    university = request.form['university']
    major = request.form['major']
    username = request.form['username']

    update_data(id, name, username, birth, sex, university, major)

    return render_template('home.html')


if __name__=='__main__':
    # app.run(host="0.0.0.0", port=5000)
    app.run(host='0.0.0.0', port=9090, debug=True)
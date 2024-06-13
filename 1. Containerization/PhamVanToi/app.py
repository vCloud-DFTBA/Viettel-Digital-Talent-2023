from flask import Flask, jsonify, render_template
import pymongo
from pymongo import MongoClient
import os

app = Flask(__name__)

def get_db():
    # client = MongoClient(host='phamvantoi',
    #                      port=27017, 
    #                      username='root', 
    #                      password='pass',
    #                     authSource="admin")

    client = MongoClient("mongodb://mongodb-server:27017/")
    db = client["internees"]
    return db


@app.route('/')
def get_stored_animals():
    db=""
    try:
        db = get_db()
        # _animals = db.internees.find()

        # response_text = ''

        # for animal in _animals:
        #     response_text += "<li>ID: " + str(animal['id']) + ", Name: " + animal['name'] + "</li>"
        

        return render_template('index.html', value = db.internees.find())
    except:
        pass
    finally:
        if type(db)==MongoClient:
            db.close()

if __name__=='__main__':
    # app.run(host="0.0.0.0", port=5000)
    app.run(host='0.0.0.0', port=9090, debug=True)

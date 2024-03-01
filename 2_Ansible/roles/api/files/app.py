from flask import Flask, jsonify, render_template
import pymongo
from pymongo import MongoClient
import os

app = Flask(__name__)


client = MongoClient("mongodb://db:27017/")
db = client["internees"]


@app.route('/')
def index():
    return render_template('index.html', attendees = db.internees.find())

if __name__=='__main__':
    app.run(host='0.0.0.0', port=9090, debug=True)
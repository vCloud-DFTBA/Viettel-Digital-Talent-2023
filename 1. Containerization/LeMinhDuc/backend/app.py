import os

from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

client = MongoClient("db:27017")
db = client.vdt


@app.route('/cloud')
def cloud():
    interns = db.cloud.find({}, {"_id": 0}).sort("id")
    return jsonify(list(interns))

import os

from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import DESCENDING, MongoClient, ReturnDocument
from dotenv import load_dotenv

load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI")

app = Flask(__name__)
CORS(app)

client = MongoClient(MONGODB_URI)
db = client.vdt


def generate_id():
    id = db.cloud.find().sort("id", DESCENDING).limit(1)
    try:
        return id[0]["id"] + 1
    except:
        return 1


@app.route("/cloud")
def get_all():
    interns = db.cloud.find({}, projection={"_id": False}).sort("id")
    return jsonify(list(interns))


@app.route("/cloud", methods=["POST"])
def create():
    data = request.get_json()
    data["id"] = generate_id()
    data["birth_year"] = int(data["birth_year"])
    db.cloud.insert_one(data)
    data.pop("_id", None)
    return jsonify(data)


@app.route("/cloud/<int:id>")
def get_one(id):
    intern = db.cloud.find_one({"id": id}, projection={"_id": False})
    return jsonify(intern)


@app.route("/cloud/<int:id>", methods=["DELETE"])
def delete(id):
    intern = db.cloud.find_one_and_delete({"id": id}, projection={"_id": False})
    return jsonify(intern)


@app.route("/cloud/<int:id>", methods=["PATCH"])
def update(id):
    data = request.get_json()
    if "birth_year" in data:
        data["birth_year"] = int(data["birth_year"])
    intern = db.cloud.find_one_and_update(
        {"id": id},
        {"$set": data},
        projection={"_id": False},
        return_document=ReturnDocument.AFTER,
    )
    return jsonify(intern)

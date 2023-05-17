from flask import jsonify, request
from pymongo import DESCENDING, ReturnDocument
from src.db import get_db


def generate_id():
    db = get_db()
    id = db.cloud.find().sort("id", DESCENDING).limit(1)
    try:
        return id[0]["id"] + 1
    except:
        return 1


class CloudController:
    @staticmethod
    def get_all():
        db = get_db()
        interns = db.cloud.find({}, projection={"_id": False}).sort("id")
        return jsonify(list(interns)), 200

    @staticmethod
    def create():
        data = request.get_json()
        data["id"] = generate_id()
        data["birth_year"] = int(data["birth_year"])
        db = get_db()
        db.cloud.insert_one(data)
        data.pop("_id", None)
        return jsonify(data), 201

    @staticmethod
    def get_one(id):
        db = get_db()
        intern = db.cloud.find_one({"id": id}, projection={"_id": False})
        if intern:
            return jsonify(intern), 200
        else:
            return jsonify({"message": "Intern not found"}), 404

    @staticmethod
    def update(id):
        data = request.get_json()
        if "birth_year" in data:
            data["birth_year"] = int(data["birth_year"])
        db = get_db()
        intern = db.cloud.find_one_and_update(
            {"id": id},
            {"$set": data},
            projection={"_id": False},
            return_document=ReturnDocument.AFTER,
        )
        if intern:
            return jsonify(intern), 200
        else:
            return jsonify({"message": "Intern not found"}), 404

    @staticmethod
    def remove(id):
        db = get_db()
        intern = db.cloud.find_one_and_delete({"id": id}, projection={"_id": False})
        if intern:
            return jsonify(intern), 200
        else:
            return jsonify({"message": "Intern not found"}), 404

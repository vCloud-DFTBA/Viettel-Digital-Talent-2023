from flask import request, jsonify
from app.controllers import intern_blueprint
from app.models.intern import Intern
from bson.objectid import ObjectId


@intern_blueprint.route("", methods=["GET"])
def get_all_interns():
    interns = Intern.get_all()
    return jsonify(interns)


@intern_blueprint.route("", methods=["POST"])
def create_intern():
    try:
        intern = Intern(
            request.json["name"],
            request.json["university"],
            request.json["year_of_birth"],
        )
        intern.save()
        return jsonify({"message": "Create successfully"})
    except:
        return jsonify({"message": "Create failed"}), 400


# Get intern by id
@intern_blueprint.route("/<id>", methods=["GET"])
def get_intern_by_id(id):
    try:
        doc_id = ObjectId(id)
        return jsonify(Intern.get_by_id(doc_id))
    except:
        return jsonify({"message": "Get failed"}), 400


# Update intern by id
@intern_blueprint.route("/<id>", methods=["PUT"])
def update_intern(id):
    try:
        doc_id = ObjectId(id)
        intern = Intern(
            request.json["name"],
            request.json["university"],
            request.json["year_of_birth"],
        )
        intern.update(doc_id)
        return jsonify({"message": "Update successfully"})
    except:
        return jsonify({"message": "Update failed"}), 400


# Delete intern by id
@intern_blueprint.route("/<id>", methods=["POST"])
def delete_intern(id):
    try:
        return jsonify(Intern.delete(id))
    except:
        return jsonify({"message": "Delete failed"}), 400


# Delete many
@intern_blueprint.route("/delete_many", methods=["POST"])
def delete_many_intern():
    ids = []
    for id in request.json["ids"]:
        ids.append(ObjectId(id))
    try:
        Intern.delete_many(ids)
        # Return 200 OK
        return jsonify({"message": "Delete successfully"})
    except:
        # Return 400 Bad Request
        return jsonify({"message": "Delete failed"}), 400


# Delete all
@intern_blueprint.route("/delete_all", methods=["POST"])
def delete_all_intern():
    try:
        Intern.delete_all()
        # Return 200 OK
        return jsonify({"message": "Delete successfully"})
    except:
        # Return 400 Bad Request
        return jsonify({"message": "Delete failed"}), 400

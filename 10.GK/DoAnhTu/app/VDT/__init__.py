import os

from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_pymongo import MongoClient


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # connect to db

    client = MongoClient(
        "mongodb://admin:Admin123@mongodb:27017/", connectTimeoutMS=3000
    )
    VDT_DB = client.VDTuser
    db = VDT_DB.user

    @app.route("/")
    def VDT():
        students = db.find()
        student_data = []

        for student in students:
            person = {
                "name": student["name"],
                "year_of_birth": student["year_of_birth"],
                "university": student["university"],
                "gender": student["gender"],
                "username": student["username"],
                "major": student["major"],
            }
            student_data.append(person)
        return render_template("VDT.html", data_student=student_data)

    @app.route("/members", methods=["GET"])
    def getlistmember():
        students = db.find()
        student_data = []

        for student in students:
            person = {
                "name": student["name"],
                "year_of_birth": student["year_of_birth"],
                "university": student["university"],
                "gender": student["gender"],
                "username": student["username"],
                "major": student["major"],
            }
            student_data.append(person)
        return jsonify(student_data)

    @app.route("/members/<username>", methods=["GET"])
    def get_student(username):
        students = db.find()
        members = []
        for student in students:
            person = {
                "name": student["name"],
                "year_of_birth": student["year_of_birth"],
                "university": student["university"],
                "gender": student["gender"],
                "username": student["username"],
                "major": student["major"],
            }
            if student["username"] == username:
                members.append(person)
        return jsonify(members)

    @app.route("/postdata", methods=["POST"])
    def post_student():
        name = request.json["name"]
        year_of_birth = request.json["year_of_birth"]
        university = request.json["university"]
        gender = request.json["gender"]
        username = request.json["username"]
        major = request.json["major"]

        db.insert_one(
            {
                "name": name,
                "year_of_birth": year_of_birth,
                "university": university,
                "gender": gender,
                "username": username,
                "major": major,
            }
        )
        return jsonify(
            {
                "name": name,
                "year_of_birth": year_of_birth,
                "university": university,
                "gender": gender,
                "username": username,
                "major": major,
            }
        )

    @app.route("/delmember/<username>", methods=["DELETE"])
    def del_mem(username):
        db.delete_one({"username": username})
        return redirect(url_for("getlistmember"))

    @app.route("/updatemember/<username>", methods=["PUT"])
    def up_mem(username):
        name = request.json["name"]
        year_of_birth = request.json["year_of_birth"]
        university = request.json["university"]
        gender = request.json["gender"]
        update_username = request.json["username"]
        major = request.json["major"]

        myquery = {"username": username}
        myupdate = {
            "$set": {
                "name": name,
                "year_of_birth": year_of_birth,
                "university": university,
                "gender": gender,
                "username": update_username,
                "major": major,
            }
        }
        db.update_one(myquery, myupdate)

        return redirect(url_for("getlistmember"))

    return app

import os

from flask import Flask, render_template, request
from flask_pymongo import MongoClient


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # connect to db

    client = MongoClient('mongodb://admin:Admin123@dbmongo:27017/', connectTimeoutMS=3000)
    VDT_DB = client.VDTuser
    db = VDT_DB.user

    # a simple page that says hello
    @app.route('/')
    def hello():

        student = db.find_one({"name": "Đỗ Anh Tú"})
        print(student)
        return str(student["name"]) + " VDT Hello"

    @app.route('/VDT')
    def VDT():
        students = db.find()
        student_data = []

        for student in students:
            person = {
                "name": student["name"],
                "birth_year": student["year_of_birth"],
                'university': student["university"],
                "gender": student["gender"],
                "username": student["username"],
                "major":student["major"]
            }
            student_data.append(person)
        print(student_data)
        return render_template("VDT.html", data_student=student_data)

    return app

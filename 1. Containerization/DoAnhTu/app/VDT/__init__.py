import os

from flask import Flask, render_template, request
from flask_pymongo import MongoClient


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # connect to db
    client = MongoClient("mongodb://user1:VDT2023@127.0.0.1:27017/VDTuser")
    VDT_DB = client.VDTuser
    db = VDT_DB.user

    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def hello():
        student = db.find_one({"name": "Đỗ Anh Tú"})
        print(student)
        return str(student["name"]) + " VDT"

    @app.route('/VDT')
    def VDT():
        students = db.find()
        student_data = []

        for student in students:
            person = {
                "name": student["name"],
                "birth_year": student["year_of_birth"],
                'university': student["university"]
            }
            student_data.append(person)
        print(student_data)
        return render_template("VDT.html", data_student=student_data)

    @app.route('/VDT/edit', methods=['POST'])
    def edit_user():
        person = {
            'name': request['name'],
            'birth_year': request['birth_year'],
            'university': request['university']
        }
        db.insert_one(person)
        return render_template("addUser.html")

    @app.route("/VDT/edit")
    def user():
        return render_template("addUser.html")

    return app

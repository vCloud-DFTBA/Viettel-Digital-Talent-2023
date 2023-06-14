from flask import Flask, request, jsonify
from init import init_data
from bson import ObjectId
from utils import insert_attendee, delete_attendee, create_student_from_form, create_formatted_student
import os
from pymongo import MongoClient


def create_app(students_collection):
    app = Flask(__name__)
    @app.route('/')
    def index():
        return "Nguyen Manh Cuong - VDT"

    @app.route('/students', methods=['GET'])
    def handle_students():
        students = list(students_collection.find())
        formatted_students = [create_formatted_student(student) for student in students]
        return jsonify(formatted_students)

    @app.route('/students/add', methods=['POST'])
    def add_students():
        student = create_student_from_form(request.form)
        insert_attendee(students_collection, student)
        return jsonify({'message': 'Student added successfully'})

    @app.route('/students/view', methods=['GET'])
    def view_student():
        student_id = request.args.get('student_id')
        student = students_collection.find_one({'_id': ObjectId(student_id)})
        formatted_student = create_formatted_student(student)
        return jsonify(formatted_student)

    @app.route('/students/edit', methods=['GET', 'POST'])
    def edit_student():
        student_id = request.args.get('student_id')
        if request.method == 'GET':
            if student_id is not None:
                student = students_collection.find_one({'_id': ObjectId(student_id)})
                if student:
                    formatted_student = create_formatted_student(student)
                    return jsonify(formatted_student)

        if request.method == 'POST':
            student = create_student_from_form(request.form)
            students_collection.update_one({"_id": ObjectId(student_id)}, {"$set": student})
            return jsonify({'message': 'Student Details Updated Successfully'})

    @app.route('/students/<student_id>', methods=['DELETE'])
    def delete_student(student_id):
        delete_attendee(students_collection, student_id)
        return jsonify({'message': 'Student Details Deleted Successfully'})
    return app


if __name__ == '__main__':
    MONGODB_DATABASE = os.environ.get("MONGODB_DATABASE")
    MONGODB_HOSTNAME = os.environ.get("MONGODB_HOSTNAME")
    uri = f'mongodb://{MONGODB_HOSTNAME}:27017'
    client = MongoClient(uri)
    db = client[f'{MONGODB_DATABASE}']
    students_collection = db.attendees
    app = create_app(students_collection)
    app.run(debug=True, use_debugger=False, use_reloader=False, host="0.0.0.0")

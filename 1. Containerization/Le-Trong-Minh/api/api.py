from flask import Flask, jsonify, request, render_template, json
from pymongo import MongoClient
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app, support_credentials=True)
client = MongoClient('mongodb://mongodb:27017/')
db = client["GFG"]

collection = db["students"]

@app.route('/', methods = ['GET'])
def index():
    listStudents = db.students.find()

    item = {}
    data = []
    for element in listStudents:
        item = {
            'id': str(element['_id']),
            'stt': str(element['stt']),
            'name': str(element['name']),
            'birth': str(element['birth']),
            'sex': str(element['sex']),
            'university': str(element['university']),
            'major': str(element['major'])
        }
        data.append(item)

    return jsonify(
        data
    )

@app.route('/student', methods = ['POST'])
def student():
    req_data = request.get_json()
    lists = req_data['lists']
    collection.insert_many(lists)

    return 'Saved!', 201


@app.route('/del', methods=['DELETE'])
def del_student():
    req_data = request.get_json()
    lists = req_data['lists']
    name = str(lists['name'])

    listStudents = db.students.find()
    for element in listStudents:
        if name == str(element['name']):
            del element
            return {'Message': 'Student has been deleted syccessfully'}


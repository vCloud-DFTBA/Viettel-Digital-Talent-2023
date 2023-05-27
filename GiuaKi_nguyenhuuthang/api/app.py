
from flask import Flask, jsonify, request, render_template, redirect, session, Response
from flask_cors import CORS
from pymongo import MongoClient
from flask_restful import Resource, Api
from bson import ObjectId
from bson.json_util import dumps
import flask
from dotenv import load_dotenv
import json
# app = Flask(__name__)
# CORS(app)

# myclient =  MongoClient("mongodb://127.0.0.1:27017/") 
# # database 
# db = myclient["data"]
   
# # Created or Switched to collection 

# collection = db["student"]

# @app.route('/api/students', methods = ['GET'])
# def students():
#     # data = []
#     # for element in collection.find():
#     #     item = {
#     #         'STT': str(element['STT']),
#     #         'Name': element['Name'],
#     #         'Year': element['Year'],
#     #         'Sex': element['Sex'],
#     #         'School': element['School'],
#     #         'Major': element['Major']
#     #     }
#     #     data.append(item)

#     # return jsonify(data)
#     STT = request.args.get('STT')
#     filter = {} if STT is None else {"STT": STT}
#     sensors = list(collection.find(filter))

#     response = Response(
#         response=dumps(sensors), status=200,  mimetype="application/json")
#     return response
  

# @app.route('/api/CreateStudent', methods=['POST'])
# def create_student():
    
#     STT = request.form['STT']
#     Name = request.form['Name']
#     Year = request.form['Year']
#     Sex = request.form['Sex']
#     School = request.form['School']
#     Major = request.form['Major']
#     student = {
#         'STT' : STT,
#         'Name': Name,
#         'Year': Year,
#         'Sex': Sex,
#         'School': School,
#         'Major': Major
#     }
#     collection.insert_one(student)

#     return jsonify({'status': 'success'})

# @app.route('/api/DeleteStudent/<STT>')
# def delete_student(STT):
#     result = collection.delete_one({'STT': ObjectId(STT)})
#     # if result:
#     #     return jsonify({'status': 'success'})
#     # else:
#     #     return jsonify({'status': 'fail'})
#     return "Delete successfully"

# @app.route('/api/GetStudent/<int:STT>', methods=[ 'POST'])
# def get_student(STT):
#     if request.method == "POST":
#         student = collection.find_one({'STT': STT})
#         if student:
#             response = {
#                 'STT': student['STT'],
#                 'Name': student['Name'],
#                 'Year': student['Year'],
#                 'Sex': student['Sex'],
#                 'School': student['School'],
#                 'Major': student['Major']
#             }
#             return json.dumps(response)
#     else:
#             return jsonify({'status': 'fail', 'message': 'student not found'})

            
# @app.route('/api/UpdateStudent/<STT>')
# def update_student(STT):
#     student = collection.find_one({'STT': ObjectId(STT)})
#     if not student:
#         return jsonify({'status': 'fail', 'message': 'student not found'})

#     # Update student information
#     student['STT'] = request.json.get('STT', student['STT'])
#     student['Name'] = request.json.get('Name', student['Name'])
#     student['Year'] = request.json.get('Year', student['Year'])
#     student['Sex'] = request.json.get('Sex', student['Sex'])
#     student['School'] = request.json.get('School', student['School'])
#     student['Major'] = request.json.get('Major', student['Major'])

#     # Save updated student to database
#     result = collection.replace_one({'STT': ObjectId(STT)}, student)
#     if result.modified_count == 1:
#         return jsonify({'status': 'success'})
#     else:
#         return jsonify({'status': 'fail'})

# if __name__ == '__main__':
#     app.run()

from flask_cors import CORS
import os
from flask import Flask, Response, request, jsonify
from dotenv import load_dotenv
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId
load_dotenv()


app = Flask(__name__)
CORS(app)
myclient =  MongoClient("mongodb://127.0.0.1:27017/") 
# database 
db = myclient["data"]
   
# Created or Switched to collection 

collection = db["student"]

@app.get("/api/getstudent")
def get_student():
    STT = request.args.get('STT')
    filter = {} if STT is None else {'STT': STT}
    sensors = list(collection.find(filter))

    response = Response(
        response=dumps(sensors), status=200,  mimetype="application/json")
    return response

@app.post("/api/addstudent")
def add_student():

    # STT = request.form['STT']
#     Name = request.form['Name']
#     Year = request.form['Year']
#     Sex = request.form['Sex']
#     School = request.form['School']
#     Major = request.form['Major']
#     student = {
#         'STT' : STT,
#         'Name': Name,
#         'Year': Year,
#         'Sex': Sex,
#         'School': School,
#         'Major': Major
#     }
    _json = request.decode('').json

    collection.insert_one(_json)
    

    resp = jsonify({"message": " added successfully"})
    resp.status_code = 200
    return resp


@app.delete("/api/deletestudent/<id>")
def delete_student(id):
    
    collection.delete_one({'_id': ObjectId(id)})

    resp = jsonify({"message": " deleted successfully"})
    resp.status_code = 200
    return resp 

@app.put("/api/updatestudent/<id>")
def update_student(id):
    _json = request.json
    collection.update_one({'_id': ObjectId(id)}, {"$set": _json})

    resp = jsonify({"message": " updated successfully"})
    resp.status_code = 200
    return resp

if __name__ == '__main__':
    app.run()
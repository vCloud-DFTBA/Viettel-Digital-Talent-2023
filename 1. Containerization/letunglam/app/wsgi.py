from flask import Flask, jsonify
import pymongo
from pymongo import MongoClient

app = Flask(__name__)

def get_db():
    client = MongoClient("mongodb://mongodb-server:27017/")
    mydb = client["students_db"]
    return mydb

@app.route("/")
def home():
    return "Hello from flask"

@app.route("/students")
def fetch_students():
    db = get_db()
    _names = db.names.find()
    names = [{"name": student["name"],
              "dob": student["dob"]} for student in _names]
    return jsonify({"students": names})

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template
import pymongo
from pymongo import MongoClient


app = Flask(__name__)

 
# Making Connection
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/") 
# database 
db = myclient["data"]
   
# Created or Switched to collection 

Collection = db["student"]

@app.route('/')
def display():
    d = db
    _student = d.student.find()
    return render_template('index.html', todos = _student)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5000, debug=True )
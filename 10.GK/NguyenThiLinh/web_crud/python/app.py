from flask import Flask, request, jsonify
import pymongo
from bson import ObjectId
from bson.json_util import dumps
client = pymongo.MongoClient('mongo_db:27017')

o = client['attendees']
db = o['attendee']

app = Flask(__name__)

@app.route('/api/attendees', methods=["GET", "POST"])
def getpost():
    if request.method == "GET":
        o = []
        for i in db.find():
            o.append({"_ID":str(ObjectId(i["_id"])), "fullName":i["fullName"],"doB":i["doB"], "gender":i["gender"], "school":i["school"], "major":i["major"]})
        return jsonify(o)
    elif request.method == "POST":
        id = db.insert_one({"fullName":request.json["fullName"],"doB":request.json["doB"],"gender":request.json["gender"],"school":request.json["school"],"major":request.json["major"]})
        return jsonify(str(id.inserted_id))

@app.route('/api/attendees/<id>', methods=["DELETE", "PUT"]) 
def deleteput(id):
    if request.method == "DELETE":
        db.delete_one({"_id":ObjectId(id)})
        return jsonify({"message":"deleted"})
    elif request.method =="PUT":
        db.update_one({"_id":ObjectId(id)}, {"$set": {
            "fullName": request.json["fullName"],
            "doB": request.json["doB"],
            "gender": request.json["gender"],
            "school": request.json["school"],
            "major": request.json["major"]
        }})
        return jsonify({"message":"updated"})

@app.route('/api/attendees/getone/<id>',methods=["GET"])
def getone(id):
    res = db.find_one({"_id":ObjectId(id)})
    return {"_ID":str(ObjectId(res["_id"])), "fullName":res["fullName"],"doB":res["doB"], "gender":res["gender"], "school":res["school"], "major":res["major"]}       
        
        

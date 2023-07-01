from flask import Flask, json, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
app.config['MONGO_URI']='mongodb://mongodb:27017/vdt23'
# app.config['MONGO_ROOT_USERNAME']='thanh'
# app.config['MONGO_ROOT_PASSWORD']='thanh'

mongo = PyMongo(app)

CORS(app)
col = mongo.db.attendee


@app.route('/api/attendees', methods=['POST'])
def createAttendee():
    col.insert_one({
        "STT": int(request.json["id"]),
        "Họ và tên": request.json["name"],
        "Năm sinh": request.json["birth"],
        "Giới tính": request.json["sex"],
        "Trường": request.json["university"],
        "Chuyên ngành": request.json["major"]
    })
    return jsonify({'id': str(request.json["id"]), 'msg': "User Added Successfully"})

@app.route('/api/attendees', methods=['GET'])
def getAttendees():
    attendees = []
    for doc in col.find():
        attendees.append({
            "id": doc["STT"],
            "name": doc["Họ và tên"],
            "birth": doc["Năm sinh"],
            "sex": doc["Giới tính"],
            "university": doc["Trường"],
            "major": doc["Chuyên ngành"]
        })
    return jsonify(attendees)


@app.route('/api/attendees/<id>', methods=['GET'])
def getAttendee(id):
    attendees = col.find_one({'STT': int(id)})
    if attendees == None:
        return jsonify({
            "id": None,
            "name": None,
            "birth": None,
            "sex": None,
            "university": None,
            "major": None
        })
    print("message " + str(attendees))
    return jsonify({
            "id": attendees["STT"],
            "name": attendees["Họ và tên"],
            "birth": attendees["Năm sinh"],
            "sex": attendees["Giới tính"],
            "university": attendees["Trường"],
            "major": attendees["Chuyên ngành"]
    })

@app.route('/api/attendees/<id>', methods=['DELETE'])
def deleteAttendee(id):
    col.delete_one({'STT': int(id)})
    return jsonify({'msg': "User Deleted Successfully"})


@app.route('/api/attendees/<id>', methods=['PUT'])
def updateAttendee(id):
    update_attendee = {'$set': {
        "STT": int(request.json["id"]),
        "Họ và tên": request.json["name"],
        "Năm sinh": request.json["birth"],
        "Giới tính": request.json["sex"],
        "Trường": request.json["university"],
        "Chuyên ngành": request.json["major"]
    }}
    col.update_one({'STT': int(id)}, update_attendee)
    return jsonify({'msg': "User Update Successfully"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

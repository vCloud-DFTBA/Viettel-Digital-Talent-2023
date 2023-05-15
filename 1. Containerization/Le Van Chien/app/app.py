from flask import Flask, request
from pymongo import MongoClient
from flask_cors import CORS, cross_origin
import json
from bson import json_util

app = Flask(__name__)
cors = CORS(app, resources={r'/people/*': {'origins': '*'}})

client = MongoClient('mongodb://db:27017')
client.drop_database('attendee')
db = client.attendee
if 'attendees' not in db.list_collection_names():
    with open('data/attendees.json') as f:
        data = json.load(f)
    db.attendees.insert_many(data)

@app.route('/people/', methods = ['GET'])
def getAll():
    attendees = json_util.dumps(db.attendees.find({}))
    return attendees

@app.route('/people/<int:num>', methods = ['GET'])
def getByID(num):
    return json_util.dumps(db.attendees.find({"id": num}))

@app.route('/people/<string:username>', methods = ['GET'])
def getByUsername(username):
    return json_util.dumps(db.attendees.find({"username": username}))

@app.route('/people/delete/<string:username>', methods = ['DELETE'])
def delete(username):
    db.attendees.delete_one({'username': username})
    return json_util.dumps({'message': f'Resource with username {username} deleted'})


@app.route('/people/create/', methods = ['PUT'])
def create():
    data = request.get_json()
    db.attendees.insert_one(data)
    return json_util.dumps({'message': 'Resource with username {} created'.format(data['username'])})

@app.route('/people/update/<string:username>', methods = ['PUT'])
def update(username):
    data = request.get_json()
    db.attendees.update_one({'username':username}, data)
    return json_util.dumps({'message': 'Resource with username {} updated'.format(username)})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

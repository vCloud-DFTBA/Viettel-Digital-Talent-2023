from flask import Flask
from pymongo import MongoClient
from flask_cors import CORS, cross_origin
import json
from bson import json_util

app = Flask(__name__)
cors = CORS(app)

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
def get(num):
    return json_util.dumps(db.attendees.find({"no": num}))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

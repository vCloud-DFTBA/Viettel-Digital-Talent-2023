from flask import Flask
from flask import jsonify
import pymongo
from bson.json_util import dumps

client = pymongo.MongoClient('mongo_db:27017')

db = client["attendees"]

col = db['attendee']

app = Flask(__name__)

@app.route('/api/attendees', methods = ['GET'])
def get_attendee():
    res = []
    print("col",col)
    for x in col.find():
        res.append(x)
    return jsonify(dumps(res))
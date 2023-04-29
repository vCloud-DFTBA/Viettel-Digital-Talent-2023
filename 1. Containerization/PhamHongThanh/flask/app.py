from flask import Flask
import pymongo
from bson.json_util import dumps

client = pymongo.MongoClient('mongodb://mongodb:27017/', username='thanh', password='thanh')
db = client["vdt23"]
collection = db['attendee']

app = Flask(__name__)

@app.route('/attendees', methods = ['GET'])
def get_attendee():
    att_list = []
    for att in collection.find():
        att_list.append(att)
    return dumps(att_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

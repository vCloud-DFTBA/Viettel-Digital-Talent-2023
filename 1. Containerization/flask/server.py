from flask import Flask
import pymongo
from bson.json_util import dumps

client = pymongo.MongoClient('mongodb://mongodb:27017/', username='thanh', password='thanh')
db = client["vdt23"]
collection = db['studentdb']

app = Flask(__name__)

@app.route('/studentdb', methods = ['GET'])
def get_student():
    student_list = []
    for att in collection.find():
        student_list.append(att)
    return dumps(student_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
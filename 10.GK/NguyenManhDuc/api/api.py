from flask import Flask, jsonify, url_for, redirect, request
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.errors import InvalidId
# from flask_restful import Api, Resource
import os
# import json

mongodb_host = os.environ.get('MONGO_HOST', '0.0.0.0')
mongodb_post = int(os.environ.get('MONGO_PORT', '27017'))
# configure the connection to the database
client = MongoClient(mongodb_host, mongodb_post)

# select the databse from mongodb
db = client.list_candidate_VDT

# select the collection (in mongodb the table is called collection)
candidate_collection = db.candidate

# candidate_collection = db.mycollection



app = Flask(__name__)


@app.route('/',methods=['GET'])
@app.route('/candidates',methods=['GET'])
def get_all_candidates():
    candidates = []
    for candidate in candidate_collection.find():
        candidates.append({
            '_id': str(candidate['_id']),
            "STT": candidate['STT'],
            "fullname": candidate['fullname'],
            "year of birth": candidate['year of birth'],
            "gender": candidate['gender'],
            "university": candidate['university'],
            "Username": candidate['Username'],
            "field": candidate['field']
        })
    return jsonify(candidates)          





@app.route('/candidates/<string:_id>', methods=['GET'])
def get_candidate(_id):
    candidates = []
    candidate=candidate_collection.find_one({"_id":ObjectId(_id)})
    if candidate:
        candidates.append({
        '_id': str(candidate['_id']),
        "STT": candidate['STT'],
        "fullname": candidate['fullname'],
        "year of birth": candidate['year of birth'],
        "gender": candidate['gender'],
        "university": candidate['university'],
        "Username": candidate['Username'],
        "field": candidate['field']
        })
        print(candidates)
        return jsonify(candidates)
    else:
        return jsonify({'message' : 'update unsucessfully'}), 404

@app.route('/candidates',methods=['POST'])
def create_candidate():
    STT = candidate_collection.count_documents({}) + 1
    fullname = request.json['fullname']
    year = request.json['year of birth']
    gender = request.json['gender']
    university = request.json['university']
    username = request.json['Username']
    field =  request.json['field']
    id = candidate_collection.insert_one({
            "STT": STT,
            "fullname": fullname,
            "year of birth": year,
            "gender": gender,
            "university": university,
            "Username": username,
            "field": field
        })
    print(id.inserted_id)
    return jsonify({'_id': str(id.inserted_id)})


@app.route("/candidates/update/<string:id>", methods=["PUT"])
def update_candidate(id):
    candidate = candidate_collection.find_one({'_id': ObjectId(id)})
    if candidate:
        # STT = request.json['STT']
        fullname = request.json['fullname']
        year = request.json['year of birth']
        gender = request.json['gender']
        university = request.json['university']
        username = request.json['Username']
        field =  request.json['field']
        candidate_collection.update_one({'_id': ObjectId(id)} , {'$set':{
            # "STT": STT,
            "fullname": fullname,
            "year of birth": year,
            "gender": gender,
            "university": university,
            "Username": username,
            "field": field
        }})
        return jsonify({'message' : 'update successfully'}), 200
    else:
        return jsonify({'message' : 'update unsucessfully'}), 404
        

@app.route('/candidates/<string:_id>',methods=["DELETE"])
def delete_candidate(_id):
    candidate = candidate_collection.find_one({'_id': ObjectId(_id)})
    if candidate:
        candidate_collection.delete_one({'_id' : ObjectId(_id)})
        return jsonify({'message': 'User deleted successfully'})
    else:
        return jsonify({'message': 'User not found'})


@app.route('/candidates/search', methods=["GET"])
def search_candidate():
    key_value=request.json
    # key=key_value
    # refer=request.json[refer]
    candidates = []
    for candidate in candidate_collection.find(key_value):
        candidates.append({
            '_id': str(candidate['_id']),
            "STT": candidate['STT'],
            "fullname": candidate['fullname'],
            "year of birth": candidate['year of birth'],
            "gender": candidate['gender'],
            "university": candidate['university'],
            "Username": candidate['Username'],
            "field": candidate['field']
        })
    return jsonify(candidates)  
    # if candidates:
    #     print(candidates)
    #     return jsonify(candidates)
    # else:
    #     print(candidates)
    #     return jsonify({'message': 'User not found'}), 404

    
    

if __name__ == "__main__":  # checking if __name__'s value is '__main__'. __name__ is an python environment variable who's value will always be '__main__' till this is the first instatnce of app.py running
    # check_empty()
    env = os.environ.get('FLASK_ENV', 'development')
    app.run(debug=True, port=5500, host="0.0.0.0")
    
    
    
    

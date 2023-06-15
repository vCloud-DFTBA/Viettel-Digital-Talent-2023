from flask import Blueprint,request
from flask_cors import cross_origin
from database.mongo import buddies_collection
from bson import ObjectId
from services.buddy_service import BuddySerivce
buddies = Blueprint("buddies",__name__)

buddy_service = BuddySerivce()

@buddies.route('/buddies')
@cross_origin()
def get_buddies():
    try:
        return buddy_service.get_buddies()
    except:
        return "Not found",404

@buddies.route('/buddies', methods=['POST'])
def add_buddy():
    try:
        
        body = request.get_json()
        buddy_reponse = buddy_service.add_buddy(body)
        return buddy_reponse, 200
    except Exception as e:
        return "",404

@buddies.route('/buddies/<id>', methods=['PUT'])
def update_buddy(id):
    try:
        body = request.get_json()
        buddy_service.update_buddy(id, body)
        return '', 200
    except Exception as e:
        return "",404

@buddies.route('/buddies/<id>', methods=['DELETE'])
def delete_buddy(id):
    try:
        buddy_service.delete_buddy(id)
        return '', 200
    except:
        return "",404
@buddies.route('/buddies/<id>')
def get_buddy(id):
    try:
        return buddy_service.get_buddy(id)
    except:
        return "",404

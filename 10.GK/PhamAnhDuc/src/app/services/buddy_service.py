from flask import Blueprint,request
from flask_cors import cross_origin
from database.mongo import buddies_collection
from bson import ObjectId


class BuddySerivce:
    def __init__(self, buddy_coll= buddies_collection) -> None:
        self.collection = buddy_coll
        
        
    def get_buddy(self,id):
        try:
            return self.collection.find_one({"_id":ObjectId(id)})
        except:
            raise RuntimeError("unable to get buddy")

    def get_buddies(self):
        try:
            return list(self.collection.find({}))
        except:
            raise RuntimeError("unable to get buddy list")

    def add_buddy(self,buddy):
        try:
            buddy_id = self.collection.insert_one(buddy).inserted_id
            return {'_id': str(buddy_id)}
        except Exception as e:
            raise RuntimeError("unable to add this buddy" )
        
    def update_buddy(self,id, buddy):
        try:
            buddy.pop("_id", None)
            self.collection.update_one({"_id":ObjectId(id)},{"$set":buddy})
            return
        except Exception as e:
            raise RuntimeError("unable to update this buddy" )

    def delete_buddy(self,id):
        try:
            self.collection.delete_one({"_id":ObjectId(id)})
            return id
        except:
            raise RuntimeError("unable to update this buddy" )
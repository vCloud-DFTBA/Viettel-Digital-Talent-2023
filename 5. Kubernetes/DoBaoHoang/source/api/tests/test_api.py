import os
from flask import Flask
from pymongo import MongoClient
from bson import ObjectId, errors
application = Flask(__name__)

DATABASE_USER = os.environ.get("DATABASE_USER")
DATABASE_PWD = os.environ.get("DATABASE_PWD")

client = MongoClient(f"mongodb://{DATABASE_USER}:{DATABASE_PWD}@db-service:27017/flaskdb?authSource=admin")
db = client['flaskdb']
collection = db.attendees

print(collection.count_documents({}))
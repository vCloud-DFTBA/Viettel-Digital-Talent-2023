import os
import pymongo
DB_URI = os.getenv("DB_URI", "mongodb://localhost:27018/")

db_client = pymongo.MongoClient(DB_URI)
db = db_client["test_database"]
buddies_collection = db["buddies"]

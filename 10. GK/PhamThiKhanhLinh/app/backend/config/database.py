from pymongo import MongoClient
from dotenv import find_dotenv, load_dotenv
import os

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
    
MONGODB_USERNAME = os.getenv("MONGODB_USERNAME")
MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")
MONGODB_DATABASE_NAME = os.getenv("MONGODB_DATABASE_NAME")
MONGODB_COLLECTION_NAME = os.getenv("MONGODB_COLLECTION_NAME")

CONNECTION_STRING = "mongodb://" + MONGODB_USERNAME + ":" + MONGODB_PASSWORD + "@localhost:27017/"
# CONNECTION_STRING = "mongodb://" + MONGODB_USERNAME + ":" + MONGODB_PASSWORD + "@mongo:27017/"

def get_database(name):
    client = MongoClient(CONNECTION_STRING)
    return client[name]

dbname = get_database(MONGODB_DATABASE_NAME)
collection_name = dbname[MONGODB_COLLECTION_NAME]

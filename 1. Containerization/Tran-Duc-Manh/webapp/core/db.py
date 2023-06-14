from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import logging
import os

MONGO_URL = os.getenv("MONGODB_URL", "mongodb://mongodb:27017/")
client = MongoClient(MONGO_URL)

try:
    # The ismaster command is cheap and does not require auth.
    logging.info(f"Trying connect to DB: {MONGO_URL}")
    client.admin.command("ismaster")
    logging.info(f"Success connect to DB: {MONGO_URL}")
except ConnectionFailure:
    logging.info("Server not available")
db_connect = client["student"]

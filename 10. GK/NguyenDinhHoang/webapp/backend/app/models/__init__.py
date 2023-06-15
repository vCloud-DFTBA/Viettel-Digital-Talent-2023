from config import Config
from pymongo import MongoClient

if Config.TESTING:
    client = MongoClient(
        host=Config.MONGO_HOST1,
        port=Config.MONGO_PORT,
        username=Config.MONGO_USERNAME,
        password=Config.MONGO_PASSWORD,
    )
else:
    client = MongoClient(
        host=[Config.MONGO_HOST1, Config.MONGO_HOST2, Config.MONGO_HOST3],
        replicaset=Config.MONGO_REPLICASET,
        port=Config.MONGO_PORT,
        username=Config.MONGO_USERNAME,
        password=Config.MONGO_PASSWORD,
    )
# check connection
print(client.server_info())
db = client["vdt-2023"]
collection = db["interns"]

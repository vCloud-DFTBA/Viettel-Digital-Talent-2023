from config import Config
from pymongo import MongoClient

client = MongoClient(
    host=Config.MONGO_HOST,
    port=Config.MONGO_PORT,
    username=Config.MONGO_USERNAME,
    password=Config.MONGO_PASSWORD
)
# check connection
print(client.server_info())
db = client['vdt-2023']
collection = db['interns']
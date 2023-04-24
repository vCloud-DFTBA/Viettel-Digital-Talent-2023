from config import Config
from pymongo import MongoClient

client = MongoClient(
    host='172.22.0.2',
    port=27017,
    username='hoangndst',
    password='Hoang2002'
)
db = client['students_db']
collection = db['students']
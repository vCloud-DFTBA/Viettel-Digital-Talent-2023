from config import Config
from pymongo import MongoClient

client = MongoClient(
    host='172.18.0.2',
    port=27017,
    username='hoangndst',
    password='Hoang2002'
)
# check connection
print(client.server_info())
# check database
print(client.list_database_names())
if 'vdt-2023' in client.list_database_names():
    print('Database already exists')
else:
    print('Database does not exists')
    # create database
    
db = client['vdt-2023']
collection = db['interns']
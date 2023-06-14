import json
import pymongo 
  
  
# Making Connection
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/") 
   
# database 
db = myclient["data"]
   
# Created or Switched to collection 

Collection = db["student"]
  
# Loading or Opening the json file
with open('tudent.json') as file:
    file_data = json.load(file)
      
# Inserting the loaded data in the Collection
# if JSON contains data more than one entry
# insert_many is used else inser_one is used
if isinstance(file_data, list):
    Collection.insert_many(file_data)  
else:
    Collection.insert_one(file_data)


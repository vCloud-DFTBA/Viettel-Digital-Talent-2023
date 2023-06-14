import os
import json
from pandas import *
from flask import Flask
from pymongo import MongoClient

client = MongoClient(os.environ['MONGO_HOST'], 27017, username=os.environ['MONGO_USERNAME'], password=os.environ['MONGO_PASSWORD'])
print('Connect to database successfully')
db = client.flask_db
attendees = db.attendees

xls = ExcelFile('./data/attendees.xlsx')
data = xls.parse(xls.sheet_names[0]).to_dict('records')

attendees.insert_many(data)
print('Insert data successfully')

app = Flask(__name__)

@app.get('/api/v1/attendee')
def getAttendees():
    response = list(attendees.find())
    for r in response: del r['_id']
    return json.dumps(response, ensure_ascii=False)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

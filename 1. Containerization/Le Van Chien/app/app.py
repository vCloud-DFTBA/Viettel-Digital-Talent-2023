from flask import Flask
from flask import render_template
from pymongo import MongoClient
import json

app = Flask(__name__)
print('start')
@app.route('/')
def hello():
    client = MongoClient('mongodb://db:27017')
    # client.drop_database('attendee')
    db = client.attendee
    if 'attendees' not in db.list_collection_names():
        with open('data/attendees.json') as f:
            data = json.load(f)
        db.attendees.insert_many(data)
    
    attendees = list(db.attendees.find({}))
    
    return render_template('index.html', attendees=attendees)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

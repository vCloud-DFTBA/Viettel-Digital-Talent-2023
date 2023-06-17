from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import pymongo
import csv
import os

app = Flask(__name__)

# Enable CORS
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

DB_URI = os.getenv("DB_URI", "mongodb://localhost:27017/")

db_client = pymongo.MongoClient(DB_URI)
db = db_client["test_database"]
buddies_collection = db["buddies"]
print("DB_URI=", DB_URI)
# Seed data
buddies = list(buddies_collection.find())

if not buddies:
    with open('attendees.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count > 0:
                buddies.append({
                    'name': row[1],
                    'yearOfBirth': row[2],
                    'gender': row[3],
                    'university': row[4],
                    'major': row[5]
                })
            line_count += 1
    buddies_collection.insert_many(buddies)


@app.route('/buddies')
@cross_origin()
def get_buddies():
    return list(buddies_collection.find({}, {'_id': 0}))


if __name__ == "__main__":
    app.run(host="0.0.0.0")

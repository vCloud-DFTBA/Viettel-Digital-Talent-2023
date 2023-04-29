from flask import Flask, render_template
from pymongo import MongoClient
# ...

app = Flask(__name__)
client = MongoClient(host='md_mongodb', port=27017, username='mongoAdmin', password='admin123', authSource='admin')

db = client.vdt2023
users = db.attendees

@app.route('/')
def index():
    all_user = users.find().sort("id")
    return render_template('index.html', users=all_user)

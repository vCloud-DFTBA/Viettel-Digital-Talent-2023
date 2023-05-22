from flask import Flask, render_template, jsonify
from pymongo import MongoClient
import os
from init import init_data

app = Flask(__name__)
DB_DATABASE = os.environ.get("DB_DATABASE")
DB_HOSTNAME = os.environ.get("DB_HOSTNAME")

client = MongoClient(f'{DB_HOSTNAME}:27017')
db = client[f'{DB_DATABASE}']

@app.route('/attendees')
def attendees_list():
    attendees = list(db.attendees.find({}))
    for attendee in attendees:
        del attendee['_id']

    return jsonify({
        "attendees": attendees
    })

@app.route('/')
def index():
    attendee = list(db.attendees.find({}))
    return render_template('index.html', data=attendee, color=os.environ.get("COLOR"))

if __name__ == '__main__':
    init_data()
    app.run(debug=True, use_debugger=False, use_reloader=False, host="0.0.0.0")
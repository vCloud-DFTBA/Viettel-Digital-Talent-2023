from flask import Flask, render_template
from pymongo import MongoClient
import os

app = Flask(__name__)
MONGODB_DATABASE = os.environ.get("MONGODB_DATABASE")
MONGODB_HOSTNAME = os.environ.get("MONGODB_HOSTNAME")

client = MongoClient(f'{MONGODB_HOSTNAME}:27017')
db = client[f'{MONGODB_DATABASE}']

@app.route('/')
def attendees_list():
    attendee = list(db.attendees.find({}))
    return render_template('index.html', data=attendee, color=os.environ.get("COLOR"))


if __name__ == '__main__':
    app.run(debug=True, use_debugger=False, use_reloader=False, host="0.0.0.0")
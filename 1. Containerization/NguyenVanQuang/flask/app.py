import os
import socket

from flask import Flask, render_template
from pymongo import MongoClient

from init import init_database

app = Flask(__name__)

MONGO_INITDB_DATABASE = os.environ.get("MONGO_INITDB_DATABASE")
SERVICE_NAME = os.environ.get("SERVICE_NAME")

client = MongoClient(f'mongodb://{SERVICE_NAME}:27017')
db = client[f'{MONGO_INITDB_DATABASE}']


@app.route('/')
def mentee_list():
    mentees = list(db.attendees.find({}))
    return render_template('index.html', data=mentees, server_name=os.environ.get("SERVER_NAME"), ip=socket.gethostbyname(socket.gethostname()))


if __name__ == '__main__':
    init_database('static/attendees.csv', db.attendees)
    app.run(debug=True, use_debugger=False, use_reloader=False, host="0.0.0.0")

from flask import Flask, render_template
from pymongo import MongoClient
import socket

from init import init_database

app = Flask(__name__)

MONGO_INITDB_DATABASE = 'vdt2023'
SERVICE_NAME = 'database'

client = MongoClient(f'mongodb://{SERVICE_NAME}:27017')
db = client[f'{MONGO_INITDB_DATABASE}']


@app.route('/')
def mentee_list():
    mentees = list(db.attendees.find({}))
    return render_template('index.html', data=mentees, ip=socket.gethostbyname(socket.gethostname()))


if __name__ == '__main__':
    init_database('static/attendees.csv', db.attendees)
    app.run(debug=True, use_debugger=False, use_reloader=False, host="0.0.0.0")

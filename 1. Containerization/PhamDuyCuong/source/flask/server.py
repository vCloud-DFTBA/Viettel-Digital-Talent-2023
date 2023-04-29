#!/usr/bin/env python
import os

from flask import Flask, render_template
from pymongo import MongoClient
from init_db import init_database
app = Flask(__name__)
MONGO_INITDB_DATABASE = 'vdt2023'
SERVICE_NAME = 'data_tier'

client = MongoClient(f'mongodb://{SERVICE_NAME}:27017')
db = client[f'{MONGO_INITDB_DATABASE}']


@app.route('/')
def todo():
    try:
        client.admin.command('ismaster')
        mentees = list(db.attendees.find({}))
        return render_template('index.html', data=mentees, border_color=os.environ.get("BORDER_COLOR"))
    except:
        return "Server not available"
    


if __name__ == "__main__":
    init_database('static/attendees.csv', db.attendees)
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9090), debug=True)


# from flask import Flask, render_template
# from pymongo import MongoClient

# from init import init_database

# app = Flask(__name__)

# MONGO_INITDB_DATABASE = 'vdt2023'
# SERVICE_NAME = 'data_tier'

# client = MongoClient(f'mongodb://{SERVICE_NAME}:27017')
# db = client[f'{MONGO_INITDB_DATABASE}']


# @app.route('/')
# def mentee_list():
#     mentees = list(db.attendees.find({}))
#     return render_template('index.html', data=mentees)


# if __name__ == '__main__':
#     init_database('static/attendees.csv', db.attendees)
#     app.run(debug=True, use_debugger=False, use_reloader=False, host="0.0.0.0")

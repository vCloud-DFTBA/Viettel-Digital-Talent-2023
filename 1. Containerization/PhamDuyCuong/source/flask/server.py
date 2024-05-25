#!/usr/bin/env python
import os

from flask import Flask, render_template
from pymongo import MongoClient
from init_db import insert_db

app = Flask(__name__)

DATABASE_NAME  = 'VDT23'
DATABASE_HOST  = 'data_tier'
client = MongoClient(DATABASE_HOST)
db = client[DATABASE_NAME]


@app.route('/')
def todo():
    try:
        client.admin.command('ismaster')
        students = list(db.attendees.find({}))
        return render_template('index.html', data= students, border_color=os.environ.get("BORDER_COLOR"))
    except:
        return "Server not available"
    

if __name__ == "__main__":
    insert_db('static/attendees.csv', db.attendees)
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT"), debug=True)


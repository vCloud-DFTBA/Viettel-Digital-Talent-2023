import os
from flask import Flask, render_template, url_for, redirect
from pymongo import MongoClient
application = Flask(__name__)

MONGODB_DATABASE = os.environ.get("MONGODB_DATABASE")
MONGODB_HOSTNAME = os.environ.get("MONGODB_HOSTNAME")

client = MongoClient(f"{MONGODB_HOSTNAME}:27017")
db = client[MONGODB_DATABASE]
collection = db.attendees

# @application.route("/")
# def index():
#     return redirect(url_for("profile"))

# @application.route("/profile")
# def profile():
#     attendees = []
#     for attendee in collection.find():
#         attendees.append(attendee)
#     return render_template("index.html", attendees=attendees)

@application.route("/profiles")
def profiles():
    attendees = []
    for attendee in collection.find():
        attendee.pop('_id', None)
        attendees.append(attendee)
    response = {
        "attendees": attendees
    }
    return response

# @application.route("/static/<path:file_path>")
# def files(file_path):
#     return url_for('static', filename=file_path)

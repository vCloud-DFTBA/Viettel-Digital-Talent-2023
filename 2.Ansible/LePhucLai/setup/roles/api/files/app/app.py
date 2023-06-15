from flask import Flask, render_template
from flask_pymongo import PyMongo

application = Flask(__name__, template_folder='template')

application.config["MONGO_URI"] = "mongodb://host_mongodb:27017/attendees"
mongo = PyMongo(application)


@application.route('/', methods=['GET'])
def index():
    cur = mongo.db.attendees.find({}, {'STT': 1, 'Name': 1, 'DOB': 1, 'Gender': 1, 'Univerity': 1, 'Major': 1, '_id': 0})
    return render_template('index.html', cur=list(cur))

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000, debug=False)

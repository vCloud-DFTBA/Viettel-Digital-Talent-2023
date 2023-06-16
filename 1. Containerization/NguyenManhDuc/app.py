from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os
import json


mongodb_host = os.environ.get('MONGO_HOST', 'localhost')
mongodb_post = int(os.environ.get('MONGO_PORT', '27017'))
# configure the connection to the database
client = MongoClient(mongodb_host, mongodb_post)


# select the databse from mongodb
db = client.list_candidate_VDT

# select the collection (in mongodb the table is called collection)
listCandi = db.candidate
title = "my dream"
heading = "THE ADVENTURE OF VIETTEL DIGITAL TALENT"


app = Flask(__name__)

def check_empty():
    if listCandi.count_documents({}) > 0:
        print('co du lieu')
    else:   
        with open('CLOUD.json') as file:
            file_data = json.load(file)
        print('khong co du lieu')
        listCandi.insert_many(file_data)
            
            
def redirect_url():
    return request.args.get('next') or \
        request.referrer or \
        url_for('index')
    
    


@app.route("/")
@app.route("/list", methods=['GET'])
def list():
    # list all value from a collection
    todos_l = listCandi.find()
    return render_template('index.html', todos=todos_l, t=title, h=heading)


if __name__ == "__main__":  # checking if __name__'s value is '__main__'. __name__ is an python environment variable who's value will always be '__main__' till this is the first instatnce of app.py running
    check_empty()
    env = os.environ.get('FLASK_ENV', 'development')   
    app.run(debug=True, port=5000,host="0.0.0.0")

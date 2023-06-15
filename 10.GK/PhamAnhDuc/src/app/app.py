import pymongo
import csv
import os
from flask import Flask
from flask_cors import CORS, cross_origin
from encoder import MyEncoder
from database.seed import seed_data
from database.mongo import buddies_collection
from resources.buddy import buddies
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

app = Flask(__name__)
app.json_encoder = MyEncoder

# Enable CORS
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.register_blueprint(buddies)
# Seed data

seed_data(buddies_collection)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

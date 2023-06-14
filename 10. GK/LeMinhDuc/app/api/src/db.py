from flask_pymongo import PyMongo

mongo = PyMongo()


def get_db():
    return mongo.db


def init_app(app):
    mongo.init_app(app)

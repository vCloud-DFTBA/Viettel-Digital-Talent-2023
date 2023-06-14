import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    MONGO_HOST = os.environ.get('MONGO_HOST')
    MONGO_PORT = int(os.environ.get('MONGO_PORT'))
    MONGO_USERNAME = os.environ.get('MONGO_USERNAME')
    MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD')
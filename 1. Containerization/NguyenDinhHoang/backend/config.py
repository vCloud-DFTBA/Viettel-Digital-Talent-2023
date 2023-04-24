import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb://hoangndst:Hoang2002@172.22.0.2:27017/vdt_intern_db'
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    MONGO_HOST1 = os.environ.get('MONGO_HOST1')
    MONGO_HOST2 = os.environ.get('MONGO_HOST2')
    MONGO_HOST3 = os.environ.get('MONGO_HOST3')
    MONGO_REPLICASET = os.environ.get('MONGO_REPLICASET')
    MONGO_PORT = int(os.environ.get('MONGO_PORT'))
    MONGO_USERNAME = os.environ.get('MONGO_USERNAME')
    MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD')
    ANSIBLE_HOST = os.environ.get('ANSIBLE_HOST')
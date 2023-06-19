import csv
import logging
import os
from pymongo import MongoClient

PATH = './data/attendees.csv'

DB_DATABASE = os.environ.get("DB_DATABASE")
DB_HOSTNAME = os.environ.get("DB_HOSTNAME")

client = MongoClient(f'{DB_HOSTNAME}:27017')
db = client[f'{DB_DATABASE}']

def init_data():
    attendee = []
    with open(PATH, encoding='utf_8_sig') as file:
        csv_reader = csv.DictReader(file, delimiter=",")
        for row in csv_reader:
            attendee.append(row)
            
        # db.attendees.insert_many(attendee)
        if db.attendees.estimated_document_count() == 0:
            logging.info("Initialize database\n")
            db.attendees.insert_many(attendee)
        else:
            logging.info("Database is already initialized\n")

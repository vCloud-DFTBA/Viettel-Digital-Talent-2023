import csv
import logging
import os
from pymongo import MongoClient

PATH = './data/attendees.csv'

MONGODB_DATABASE = os.environ.get("MONGODB_DATABASE")
MONGODB_HOSTNAME = os.environ.get("MONGODB_HOSTNAME")

client = MongoClient(f'{MONGODB_HOSTNAME}:27017')
db = client[f'{MONGODB_DATABASE}']

if __name__ == '__main__':
    attendee = []
    with open(PATH, encoding='utf_8_sig') as file:
        csv_reader = csv.DictReader(file, delimiter=",")
        for row in csv_reader:
            attendee.append(row)

    if db.attendees.estimated_document_count() == 0:
        logging.info("Initialize database\n")
        db.attendees.insert_many(attendee)
    else:
        logging.info("Database is already initialized\n")
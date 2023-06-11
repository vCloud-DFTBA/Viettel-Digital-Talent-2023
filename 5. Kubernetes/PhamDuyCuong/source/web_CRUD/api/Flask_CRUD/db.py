import csv
import os
import logging
from pymongo import MongoClient


def init_db(path_to_csv):
    logger = logging.getLogger()
    DATABASE_URL = os.environ.get('DATABASE_URL')
    DATABASE_NAME = "VDT2023"
    try:
        client = MongoClient(DATABASE_URL)
        db = client[DATABASE_NAME]
        collection = db.attendees
        if collection.estimated_document_count() == 0:
            rows = []
            csvFile = open(path_to_csv, encoding="utf-8")
            csv_reader = csv.DictReader(csvFile, delimiter=";")
            for row in csv_reader:
                rows.append(row)
            collection.insert_many(rows)
        logger.warning("Conected to database")
        return collection
    except BaseException:
        logger = logging.getLogger()
        logger.warning("Cann't connect to database")
        return None

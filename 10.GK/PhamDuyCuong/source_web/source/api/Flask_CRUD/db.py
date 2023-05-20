import csv
import logging
from pymongo import MongoClient


def init_db(path_to_csv="../static/attendees.csv"):
    DATABASE_NAME = "VDT23"
    DATABASE_HOST = "localhost"
    try:
        client = MongoClient("mongodb://localhost:27017/")
        db = client[DATABASE_NAME]
        collection = db.attendees

        if collection.estimated_document_count() == 0:
            logging.info("Initialize database\n")
            rows = []
            csvFile = open(path_to_csv, encoding="utf-8")
            csv_reader = csv.DictReader(csvFile, delimiter=";")
            for row in csv_reader:
                rows.append(row)
            collection.insert_many(rows)

        return collection
    except BaseException:
        logger = logging.getLogger()
        logger.warning("Cann't connect to database")
        return None

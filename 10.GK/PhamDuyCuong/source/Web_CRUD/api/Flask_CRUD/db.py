import csv
import logging
from pymongo import MongoClient

def init_db(path_to_csv):
    DATABASE_NAME = "VDT23"
    DATABASE_HOST = "localhost"
    logger = logging.getLogger()
    try:
        client = MongoClient(DATABASE_HOST)
        db = client[DATABASE_NAME]
        collection = db.attendees
        logger.warning("Conected to database")

        if collection.estimated_document_count() == 0:
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

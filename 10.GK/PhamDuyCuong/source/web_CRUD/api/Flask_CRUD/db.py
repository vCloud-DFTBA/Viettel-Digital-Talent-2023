import csv
import logging
from pymongo import MongoClient


def init_db(path_to_csv):
    DB_HOSTNAME = "ec2-44-201-231-16.compute-1.amazonaws.com:27017/"
    DATABASE_NAME = "VDT2023"
    logger = logging.getLogger()
    try:
        MONGO_URI = f"mongodb://{DB_HOSTNAME}"
        client = MongoClient(MONGO_URI)
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

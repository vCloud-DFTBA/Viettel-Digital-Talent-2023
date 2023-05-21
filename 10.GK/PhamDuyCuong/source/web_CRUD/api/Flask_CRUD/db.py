import csv
import logging
from pymongo import MongoClient


def init_db(path_to_csv):
    DB_HOSTNAME="44.201.231.16"
    DB_USERNAME="admin"
    DB_PASSWORD="vdt23"
    DATABASE_NAME="VDT2023"
    logger = logging.getLogger()
    try:
        MONGO_URI =f"mongodb://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}:27017"
        print(MONGO_URI)
        client = MongoClient(MONGO_URI)
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

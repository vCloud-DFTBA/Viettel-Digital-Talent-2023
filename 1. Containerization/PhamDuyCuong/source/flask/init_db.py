import csv
import logging


def init_database(path, collection):
    payload = []

    with open(path, encoding='utf-8') as file:
        csv_reader = csv.DictReader(file, delimiter=";")
        for row in csv_reader:
            payload.append(row)

    # if collection.estimated_document_count() == 0:
    #    logging.info("Initialize database\n")
    collection.insert_many(payload)
    #else:
    #    logging.info("Database is already initialized\n")
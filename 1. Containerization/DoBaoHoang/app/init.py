import csv

def init_database(path, collection):
    if collection.count_documents({}) == 0:
        with open(path, "r", encoding='utf_8_sig') as file:
            data = csv.DictReader(file, delimiter=",")
            for row in data:
                collection.insert_one(row)

if __name__ == "__main__":
    import os
    from pymongo import MongoClient

    MONGODB_DATABASE = os.environ.get("MONGODB_DATABASE")
    MONGODB_HOSTNAME = os.environ.get("MONGODB_HOSTNAME")

    client = MongoClient(f"{MONGODB_HOSTNAME}:27017")
    db = client[MONGODB_DATABASE]
    collection = db.attendees

    init_database('static/attendees.csv', collection)
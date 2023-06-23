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

    DATABASE_USER = os.environ.get("DATABASE_USER")
    DATABASE_PWD = os.environ.get("DATABASE_PWD")

    client = MongoClient(f"mongodb://{DATABASE_USER}:{DATABASE_PWD}@db-service:27017/flaskdb?authSource=admin")
    db = client['flaskdb']
    collection = db.attendees

    init_database('static/attendees.csv', collection)
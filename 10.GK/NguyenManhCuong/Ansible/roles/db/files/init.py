import csv
from pymongo import MongoClient
import os


def insert_attendee(collection, attendee):
    if collection.find_one(sort=[("stt", -1)]):
        attendee['stt'] = int(collection.find_one(sort=[("stt", -1)])["stt"]) + 1
    else:
        attendee['stt'] = 1
    result = collection.insert_one(attendee)
    return result

def init_data(students_collection):
    
    if students_collection.estimated_document_count() == 0:
        csv_path = './roles/files/attendees.csv'
        with open(csv_path, encoding='utf-8-sig') as file:
            csv_reader = csv.DictReader(file, delimiter=";")
            students = list(csv_reader)
        if students:
            for student in students:
                insert_attendee(students_collection, student)
            print("Database initialized with data from the CSV file.")
        else:
            print("The CSV file is empty.")
    else:
        print("Database is already initialized!")
    return students_collection

if __name__ == '__main__':
    MONGODB_DATABASE = os.environ.get("MONGODB_DATABASE")
    MONGODB_HOSTNAME = os.environ.get("MONGODB_HOSTNAME")
    client = MongoClient(f"{MONGODB_HOSTNAME}:27017")
    db = client[f'{MONGODB_DATABASE}']
    students_collection = db.attendees
    init_data(students_collection)
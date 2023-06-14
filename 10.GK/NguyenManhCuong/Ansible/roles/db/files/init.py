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
        csv_path = '/tmp/files/attendees.csv'
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
    MONGODB_DATABASE = 'database'
    MONGODB_HOSTNAME = 'ec2-54-166-186-66.compute-1.amazonaws.com'
    client = MongoClient(f"mongodb://{MONGODB_HOSTNAME}:27017")
    db = client[f'{MONGODB_DATABASE}']
    students_collection = db.attendees
    init_data(students_collection)
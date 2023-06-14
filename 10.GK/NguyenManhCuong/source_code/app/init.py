# import csv
# from utils import insert_attendee
# from pymongo import MongoClient


# def init_data(database, host_name):
#     MONGODB_DATABASE = database
#     MONGODB_HOSTNAME = host_name
#     client = MongoClient(f'{MONGODB_HOSTNAME}:27017')
#     db = client[f'{MONGODB_DATABASE}']
#     students_collection = db.attendees
#     if students_collection.estimated_document_count() == 0:
#         csv_path = './data/attendees.csv'
#         with open(csv_path, encoding='utf-8-sig') as file:
#             csv_reader = csv.DictReader(file, delimiter=";")
#             students = list(csv_reader)
#         if students:
#             for student in students:
#                 insert_attendee(students_collection, student)
#             print("Database initialized with data from the CSV file.")
#         else:
#             print("The CSV file is empty.")
#     else:
#         print("Database is already initialized!")
#     return students_collection
import csv
from utils import insert_attendee
from pymongo import MongoClient
import os

def init_data(students_collection):
    
    if students_collection.estimated_document_count() == 0:
        csv_path = './data/attendees.csv'
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

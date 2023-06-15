import csv
from os import path, getenv

dir_path = path.dirname(path.realpath(__file__))
force_seed_data = getenv("FORCE_SEED_DATA",False)
def seed_data(collection):
    buddies = list(collection.find())

    if force_seed_data:
        collection.delete_many({})
        buddies = []

    if not buddies:
        with open(dir_path +'/attendees.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count > 0:
                    buddies.append({
                        'name': row[1],
                        'yearOfBirth': row[2],
                        'gender': row[3],
                        'university': row[4],
                        'major': row[5]
                    })
                line_count += 1
        collection.insert_many(buddies)
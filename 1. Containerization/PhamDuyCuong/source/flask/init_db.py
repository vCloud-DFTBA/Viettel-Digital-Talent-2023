import csv

def insert_db(path, collection):
    rows = []
    csvFile = open(path, encoding='utf-8')
    csv_reader = csv.DictReader(csvFile, delimiter=";")
    for row in csv_reader:
        rows.append(row)
    print(rows)
    collection.insert_many(rows)

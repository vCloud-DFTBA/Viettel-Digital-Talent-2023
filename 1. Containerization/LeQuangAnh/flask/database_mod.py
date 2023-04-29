import csv
def create_database(db):
    with open('static/attendees.csv', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = []
        for row in reader:
            rows.append(row)
        db.mytable.insert_many(rows)

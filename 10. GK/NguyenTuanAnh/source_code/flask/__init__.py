import csv
import logging
import os

from app import create_app

if __name__ == "__main__":
    app, mysql = create_app('many random bytes', os.environ['MYSQL_HOST'], os.environ['MYSQL_USER'],
                            os.environ['MYSQL_PASSWORD'], os.environ['MYSQL_DB'])

    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendees (
            id int not null auto_increment,
            name varchar(255),
            username varchar(255),
            birth_year int,
            gender varchar(255),
            university varchar(255),
            major varchar(255),
            PRIMARY KEY (id)
        )
        """)
        mysql.connection.commit()

        with open('./static/data/attendees.csv', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file, delimiter=";")

            cursor.execute("SELECT COUNT(*) FROM attendees ORDER BY id")
            count = cursor.fetchall()
            log = logging.getLogger()

            if count[0][0] == 0:
                for row in csv_reader:
                    name = row['name']
                    username = row['username']
                    birth_year = int(row['birth_year'])
                    gender = row['gender']
                    university = row['university']
                    major = row['major']

                    cursor.execute(
                        "INSERT INTO attendees (name, username, birth_year, gender, university, major) "
                        "VALUES (%s, %s, %s, %s, %s, %s)",
                        (name, username, birth_year, gender, university, major))
                    mysql.connection.commit()

        cursor.close()

    app.run(debug=True, host="0.0.0.0")

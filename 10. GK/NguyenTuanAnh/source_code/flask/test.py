import os
import unittest

from app import create_app


class TestStudent(unittest.TestCase):
    def setUp(self):
        # self.app, self.mysql = create_app('many random bytes', os.environ['MYSQL_HOST'], os.environ['MYSQL_USER'], os.environ['MYSQL_PASSWORD'], os.environ['MYSQL_DB'])
        self.app, self.mysql = create_app('many random bytes',
                                          '3.226.18.226',
                                          'admin',
                                          'nguyentuananh',
                                          'crudapptest')
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

        with self.app.app_context():
            cursor = self.mysql.connection.cursor()
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
            );
            INSERT INTO attendees (name, username, birth_year, gender, university, major) \
            VALUES ('Le Quang Anh', 'anhlq', 1997, 'Nam', 'ITMO', 'An toàn thông tin'),
                   ('Phạm Huy Hoàng', 'hoangph', 1997, 'Nam', 
                   'ITMO', 'An toàn thông tin');
            """)

            cursor.close()
            cursor = self.mysql.connection.cursor()
            self.mysql.connection.commit()

            cursor.execute("SELECT * FROM attendees")
            result = cursor.fetchall()
            self.mysql.connection.commit()
            print(result)

            cursor.close()

    def tearDown(self):
        with self.app.app_context():
            cursor = self.mysql.connection.cursor()
            cursor.execute("DROP TABLE attendees")
            self.mysql.connection.commit()
            cursor.close()

    def test_add_student(self):
        self.client.post('/insert', data={'name': 'Nguyen Tuan Anh', 'username': 'anhnt', 'birth_year': 1997,
                                          'gender': 'Nam', 'university': 'ITMO', 'major': 'An toàn thông tin'})

        result = []
        with self.app.app_context():
            cursor = self.mysql.connection.cursor()
            cursor.execute("SELECT * FROM attendees")
            result = cursor.fetchall()
            self.mysql.connection.commit()
            cursor.close()

        self.assertEqual(len(result), 3)
        self.assertEqual(result[2][0], 3)
        self.assertEqual(result[2][1], 'Nguyen Tuan Anh')
        self.assertEqual(result[2][2], 'anhnt')
        self.assertEqual(result[2][3], 1997)
        self.assertEqual(result[2][4], 'Nam')
        self.assertEqual(result[2][5], 'ITMO')
        self.assertEqual(result[2][6], 'An toàn thông tin')

    def test_update_student(self):
        self.client.post('/update', data={'id': 1, 'name': 'Le Quang Anh', 'username': 'anhlq',
                                          'birth_year': 1998, 'gender': 'Nam',
                                          'university': 'ITMO', 'major': 'An toàn thông tin'})

        result = []
        with self.app.app_context():
            cursor = self.mysql.connection.cursor()
            cursor.execute("SELECT * FROM attendees")
            result = cursor.fetchall()
            self.mysql.connection.commit()
            cursor.close()

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0][0], 1)
        self.assertEqual(result[0][1], 'Le Quang Anh')
        self.assertEqual(result[0][2], 'anhlq')
        self.assertEqual(result[0][3], 1998)
        self.assertEqual(result[0][4], 'Nam')
        self.assertEqual(result[0][5], 'ITMO')
        self.assertEqual(result[0][6], 'An toàn thông tin')

    def test_delete_student(self):
        result = []
        with self.app.app_context():
            cursor = self.mysql.connection.cursor()
            cursor.execute("DELETE FROM attendees WHERE id=1")
            cursor.execute("SELECT * FROM attendees")
            result = cursor.fetchall()
            self.mysql.connection.commit()
            cursor.close()

        self.assertEqual(len(result), 1)


if __name__ == '__main__':
    unittest.main()

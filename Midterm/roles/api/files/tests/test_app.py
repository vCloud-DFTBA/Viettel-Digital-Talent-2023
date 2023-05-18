import unittest
from pymongo import MongoClient

class SetupTests(unittest.TestCase):
    def setUp(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["internees"]
        if self.db.internees.count_documents({}) == 0:
            self.db.internees.insert_one({
                'id': '1',
                'name': 'Vinh dep trai 1',
                'username': 'vinhnd',
                'birth': '2002',
                'sex': 'Nam',
                'university': 'PTIT',
                'major': 'IT'
            })

    def tearDown(self):
        self.db.internees.drop()
        self.client.close()

    def test_get_all_student(self):
        count = self.db.internees.count_documents({})
        self.assertEqual(count, 1)

        document = self.db.internees.find_one({'id': '1'})
        self.assertEqual(document['name'], 'Vinh dep trai 1')
        self.assertEqual(document['username'], 'vinhnd')

    def test_add_Student(self):
        self.db.internees.insert_one({
            'id': '2',
            'name': 'Vinh dep trai 2',
            'username': 'vinhnd',
            'birth': '2002',
            'sex': 'Nam',
            'university': 'PTIT',
            'major': 'IT'
        })
        count = self.db.internees.count_documents({})
        self.assertEqual(count, 2)

    def test_update_Student(self):
        self.db.internees.update_one(
            {'id': '1'},
            {"$set": {
                'name': 'Vinh dep trai 2',
                'username': 'vinhnd',
                'birth': '2002',
                'sex': 'Nam',
                'university': 'PTIT',
                'major': 'IT'
            }}
        )

        document = self.db.internees.find_one({'id': '1'})
        self.assertEqual(document['name'], 'Vinh dep trai 2')

    def test_delete_Student(self):
        self.db.internees.delete_one({'id': '2'})
        count = self.db.internees.count_documents({})
        self.assertEqual(count, 1)

    def test_view_Stuent(self):
        student = self.db.internees.find_one({'id': '1'}, {"_id": 0})
        self.assertEqual(student['name'], 'Vinh dep trai 1')

if __name__ == "__main__":
    unittest.main()

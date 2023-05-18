import requests
import json
import unittest


class AppTestCase(unittest.TestCase):
    base_url = 'http://localhost:81'

    def test_list_route(self):
        response = requests.get(f'{self.base_url}/list')
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIsInstance(data, list)

    def test_add_student_route(self):
        student_data = {
            'id': 1,
            'name': 'John Doe',
            'username': 'johndoe',
            'birth': 1995,
            'sex': 'Male',
            'university': 'XYZ University',
            'major': 'Computer Science'
        }

        response = requests.post(f'{self.base_url}/addStudent', json=student_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers['Content-Type'], 'application/json')

        data = response.json()
        self.assertEqual(data['message'], 'Student added successfully')

    def test_delete_student_route(self):
        student_id = 1

        response = requests.delete(f'{self.base_url}/deleteStudent/{student_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json')

        data = response.json()
        self.assertEqual(data['message'], 'Student deleted successfully')

    def test_view_student_route(self):
        student_id = 1

        response = requests.get(f'{self.base_url}/view/{student_id}')
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 1)

    def setUp(self):
        self.base_url = 'http://localhost:81'


if __name__ == '__main__':
    unittest.main()

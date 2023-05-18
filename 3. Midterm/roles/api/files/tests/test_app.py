import unittest
import requests


URL = "http://127.0.0.1:9090"


class TestApp(unittest.TestCase):

    # Test web page.
    def test_get_all_students(self):
        response = requests.get(f"{URL}/list")
        self.assertEqual(response.status_code, 200)

    def test_insert_student(self):
        data = {
            'id': 37,
            'name': 'Bùi Minh Sơn',
            'username': 'minhson',
            'birth': 2002,
            'sex': 'Nam',
            'university': 'Đại học Công nghệ - Đại học Quốc gia Hà Nội',
            'major': 'Công nghệ thông tin'
        }
        response = requests.post(f"{URL}/addStudent", json=data)
        self.assertEqual(response.status_code, 201)

    def test_delete_student(self):
        response = requests.delete(f"{URL}/deleteStudent/29")
        self.assertEqual(response.status_code, 200)

    def test_get_by_id(self):
        response = requests.get(f"{URL}/view/29")
        self.assertEqual(response.status_code, 200)

    def test_update_student(self):
        data = {
            'name': 'Bùi Minh Sơn',
            'username': 'minhson',
            'birth': 2002,
            'sex': 'Nam',
            'university': 'Đại học Công nghệ - Đại học Quốc gia Hà Nội',
            'major': 'Công nghệ thông tin'
        }
        response = requests.put(f"{URL}/updateStudent/29", json=data)
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
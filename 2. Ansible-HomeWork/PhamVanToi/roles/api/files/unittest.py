import unittest
from app import app


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_read_page(self):
        response = self.app.get('/read')
        self.assertEqual(response.status_code, 200)

    def test_create_page(self):
        response = self.app.get('/create')
        self.assertEqual(response.status_code, 200)

    def test_delete_page(self):
        response = self.app.get('/delete')
        self.assertEqual(response.status_code, 200)

    def test_update_page(self):
        response = self.app.get('/update')
        self.assertEqual(response.status_code, 200)

    def test_create_data(self):
        data = {
            'id': 'test_id',
            'name': 'test_name',
            'sex': 'test_sex',
            'birth': 'test_birth',
            'university': 'test_university',
            'major': 'test_major',
            'username': 'test_username'
        }
        response = self.app.post('/create', data=data)
        self.assertEqual(response.status_code, 200)

    def test_delete_data(self):
        data = {
            'id': 'test_id'
        }
        response = self.app.post('/delete', data=data)
        self.assertEqual(response.status_code, 200)

    def test_update_data(self):
        data = {
            'id': 'test_id',
            'name': 'test_name_updated',
            'sex': 'test_sex_updated',
            'birth': 'test_birth_updated',
            'university': 'test_university_updated',
            'major': 'test_major_updated',
            'username': 'test_username_updated'
        }
        response = self.app.post('/update', data=data)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()

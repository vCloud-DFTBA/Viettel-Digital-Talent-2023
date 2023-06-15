import unittest
from unittest import mock

from bson import ObjectId
from api import app

class BackendTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_vdt_endpoint(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), 'Bui Minh Son - VDT')

    def test_users_endpoint(self):
        with mock.patch('api.collection.find') as mock_find:
            mock_find.return_value = [
                {
                    '_id': '1',
                    'Name': 'John Doe',
                    'YearOfBirth': 1990,
                    'Sex': 'Male',
                    'School': 'ABC School',
                    'Major': 'Computer Science'
                },
                {
                    '_id': '2',
                    'Name': 'Jane Smith',
                    'YearOfBirth': 1995,
                    'Sex': 'Female',
                    'School': 'XYZ School',
                    'Major': 'Data Science'
                }
            ]

            response = self.app.get('/users')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.json), 2)
            self.assertEqual(response.json[0]['Name'], 'John Doe')
            self.assertEqual(response.json[1]['Major'], 'Data Science')


    def test_save_user_endpoint(self):
        with mock.patch('api.collection.insert_one') as mock_insert_one:
            response = self.app.post('/user', json={
                'Name': 'John Doe',
                'YearOfBirth': 1990,
                'Sex': 'Male',
                'School': 'ABC School',
                'Major': 'Computer Science'
            })
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'status': 'success'})
            mock_insert_one.assert_called_once()
    def test_delete_user_endpoint(self):
        user_id = ObjectId('626bccb9697a12204fb22ea3')

        with mock.patch('api.collection.delete_one') as mock_delete_one:
            mock_delete_one.return_value.deleted_count = 1

            response = self.app.delete(f'/user/{user_id}')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'status': 'success'})
            mock_delete_one.assert_called_once_with({'_id': mock.ANY})

    def test_get_user_endpoint(self):
        user_id = ObjectId('626bccb9697a12204fb22ea3')
        user_data = {
            '_id': user_id,
            'Name': 'John Doe',
            'YearOfBirth': 1990,
            'Sex': 'Male',
            'School': 'ABC School',
            'Major': 'Computer Science'
        }

        with mock.patch('api.collection.find_one') as mock_find_one:
            mock_find_one.return_value = user_data

            response = self.app.get(f'/user/{user_id}')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['Name'], 'John Doe')
            mock_find_one.assert_called_once_with({'_id': mock.ANY})

    def test_update_user_endpoint(self):
        user_id = ObjectId('626bccb9697a12204fb22ea3')
        user_data = {
            '_id': user_id,
            'Name': 'John Doe',
            'YearOfBirth': 1990,
            'Sex': 'Male',
            'School': 'ABC School',
            'Major': 'Computer Science'
        }

        updated_user_data = {
            'Name': 'John Doe'
        }

        with mock.patch('api.collection.find_one') as mock_find_one, \
            mock.patch('api.collection.replace_one') as mock_replace_one:
            mock_find_one.return_value = user_data
            mock_replace_one.return_value = mock.MagicMock(modified_count=1)
    
            response = self.app.put(f'/user/{user_id}', json=updated_user_data)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'status': 'success'})
            mock_find_one.assert_called_once_with({'_id': user_id})
            mock_replace_one.assert_called_once_with({'_id': user_id}, mock.ANY)
    
    # Add more test cases for other endpoints...

if __name__ == '__main__':
    unittest.main()
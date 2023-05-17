import unittest
from unittest.mock import patch, MagicMock
from backend.app import app

class TestApp(unittest.TestCase):
    @patch('pymongo.collection.Collection.find')
    def test_getAllAttendees(self, mock_find):
        mock_cursor = MagicMock()
        mock_cursor.sort.return_value = mock_cursor
        mock_cursor.__iter__.return_value = [
            {'id': '1', 'name': 'John', 'birthyear': '2000', 'gender': 'male', 'university': 'ABC', 'major': 'CS'},
            {'id': '2', 'name': 'Mary', 'birthyear': '1998', 'gender': 'female', 'university': 'DEF', 'major': 'IT'}
        ]
        mock_find.return_value = mock_cursor
        response = app.test_client().get('/attendees')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['id'], 1)
        self.assertEqual(data[1]['name'], 'Mary')

    @patch('pymongo.collection.Collection.find_one')
    def test_getAttendeeById(self, mock_find_one):
        mock_attendee = {'id': 1, 'name': 'popi', 'birthyear': 1990, 'gender': 'Male', 'university': 'XYZ', 'major': 'CS'}
        mock_find_one.return_value = mock_attendee
        
        response = app.test_client().get('/attendee/1')
        data = response.get_json()
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, mock_attendee)

    @patch('pymongo.collection.Collection.find_one')
    def test_getAttendeeById_NotFound(self, mock_find_one):
        mock_find_one.return_value = None
        
        response = app.test_client().get('/attendee/10000')
        data = response.get_json()
        
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['message'], 'Attendee Not Found')
    
    @patch('pymongo.collection.Collection.find_one')
    @patch('pymongo.collection.Collection.insert_one')
    def test_addAttendee(self, mock_insert_one,  mock_find_one):
        attendee = {'id': 1, 'name': 'BinhChi', 'birthyear': 1990, 'gender': 'Male', 'university': 'XYZ', 'major': 'CS'}
        mock_find_one.return_value = None
        mock_insert_one.return_value = 1
        response = app.test_client().post('/add', json = attendee)
        data = response.get_json()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['message'], 'Add successfully')

    @patch('pymongo.collection.Collection.find_one')
    @patch('pymongo.collection.Collection.insert_one')
    def test_addAttendee_Exist(self, mock_insert_one,  mock_find_one):
        newAttendee = {'id': 1, 'name': 'BinhChi', 'birthyear': 1990, 'gender': 'Male', 'university': 'XYZ', 'major': 'CS'}
        mock_find_one.return_value = {'id': 1}
        mock_insert_one.return_value = 1
        response = app.test_client().post('/add', json = newAttendee)
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['message'], 'Exist Attendee with same id')

    @patch('pymongo.collection.Collection.find_one')
    @patch('pymongo.collection.Collection.update_one')
    def test_updateAttendee(self, mock_update_one, mock_find_one):
        updatedAttendee = {'id': 1, 'name': 'BinhChi', 'birthyear': 1990, 'gender': 'Male', 'university': 'XYZ', 'major': 'CS'}
        mock_find_one.return_value = {'id': 1, 'name': 'NewBinh', 'birthyear': 1990, 'gender': 'Male', 'university': 'XYZ', 'major': 'CS'}
        mock_update_result = MagicMock(modified_count = 1)
        mock_update_one.return_value = mock_update_result

        response = app.test_client().put('/update/1', json = updatedAttendee)
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Edit successfully')

    @patch('pymongo.collection.Collection.find_one')
    @patch('pymongo.collection.Collection.update_one')
    def test_updateAttendee_NotExist(self, mock_update_one, mock_find_one):
        updatedAttendee = {'id': 1, 'name': 'BinhChi', 'birthyear': 1990, 'gender': 'Male', 'university': 'XYZ', 'major': 'CS'}
        mock_find_one.return_value = None
        mock_update_result = MagicMock(modified_count = 0)
        mock_update_one.return_value = mock_update_result

        response = app.test_client().put('/update/1', json = updatedAttendee)
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['message'], 'Attendee Not Found')

    @patch('pymongo.collection.Collection.find_one')
    @patch('pymongo.collection.Collection.update_one')
    def test_updateAttendee_NoChange(self, mock_update_one, mock_find_one):
        updatedAttendee = {'id': 1, 'name': 'BinhChi', 'birthyear': 1990, 'gender': 'Male', 'university': 'XYZ', 'major': 'CS'}
        mock_find_one.return_value = {'id': 1, 'name': 'BinhChi', 'birthyear': 1990, 'gender': 'Male', 'university': 'XYZ', 'major': 'CS'}
        mock_update_result = MagicMock(modified_count = 0)
        mock_update_one.return_value = mock_update_result

        response = app.test_client().put('/update/1', json = updatedAttendee)
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'No attendee updated')

    @patch('pymongo.collection.Collection.delete_one')
    def test_deleteAttendee(self, mock_delete_one):
        mock_delete_result = MagicMock(deleted_count = 1)
        
        mock_delete_one.return_value = mock_delete_result
        response = app.test_client().delete('/delete/1')

        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Delete successfully')
    
    @patch('pymongo.collection.Collection.delete_one')
    def test_deleteAttendee_NotExist(self, mock_delete_one):
        mock_delete_result = MagicMock(deleted_count = 0)
        
        mock_delete_one.return_value = mock_delete_result
        response = app.test_client().delete('/delete/1')
        
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'No attendee deleted')
    

if __name__== '__main__':
    unittest.main()


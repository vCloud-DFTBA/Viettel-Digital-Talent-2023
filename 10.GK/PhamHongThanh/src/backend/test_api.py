import unittest
from unittest import mock
from app import app


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_all_attendees(self):
        with mock.patch('app.col.find') as mock_find:
            mock_find.return_value = [
                {
                "STT": 1,
                "Họ và tên": "Bùi Minh Sơn",
                "Năm sinh": 2002,
                "Giới tính": "Nam",
                "Trường": "Đại học Công nghệ - Đại học Quốc gia Hà Nội",
                "Chuyên ngành": "Công nghệ thông tin"
                },
                {
                "STT": 2,
                "Họ và tên": "Đào Đại Hiệp",
                "Năm sinh": 2001,
                "Giới tính": "Nam",
                "Trường": "Đại học Bách khoa Hà Nội",
                "Chuyên ngành": "Điện tử viễn thông"
                }
            ]
            response = self.app.get('/api/attendees')
            self.assertEqual(len(response.json), 2)
            self.assertEqual(response.json[0]['name'], 'Bùi Minh Sơn')
            self.assertEqual(response.json[0]['major'], 'Công nghệ thông tin')

    def test_create_attendee(self):
        with mock.patch('app.col.insert_one') as mock_insert_one:
            response = self.app.post('/api/attendees', json={
                'id': 36,
                'name': 'pham',
                'birth': 1998,
                'sex': 'Male',
                'university': 'HUST',
                'major': 'ATTT'
            })
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'id': '36', 'msg': 'User Added Successfully'})
            mock_insert_one.assert_called_once()

    def test_delete_attendees(self):
        with mock.patch('app.col.delete_one') as mock_delete_one:
            mock_delete_one.return_value.deleted_count = 1
            response = self.app.delete('/api/attendees/1')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'msg': 'User Deleted Successfully'})
            mock_delete_one.assert_called_once_with({'STT': mock.ANY})

    def test_get_attendee(self):
        
        mock_attendee =  {
                "STT": 1,
                "Họ và tên": "Bùi Minh Sơn",
                "Năm sinh": 2002,
                "Giới tính": "Nam",
                "Trường": "Đại học Công nghệ - Đại học Quốc gia Hà Nội",
                "Chuyên ngành": "Công nghệ thông tin"
                }
        with mock.patch('app.col.find_one') as mock_find_one:
            mock_find_one.return_value = mock_attendee
            response = self.app.get('/api/attendees/1')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['name'], 'Bùi Minh Sơn')

    def test_update_attendee(self):
        
        mock_attendee = {
            "STT": 1,
            "Họ và tên": "Bùi Minh Sơn",
            "Năm sinh": 2002,
            "Giới tính": "Nam",
            "Trường": "Đại học Công nghệ - Đại học Quốc gia Hà Nội",
            "Chuyên ngành": "Công nghệ thông tin"
        }

        updated_mock_attendee = {
            'id': 1,
            'name': "Bùi Minh Sơn",
            'sex' : "Nam",
            'birth': '2004',
            'university': "HUST",
            'major' : "ATTT"
        }

        with mock.patch('app.col.find_one') as mock_find_one, \
            mock.patch('app.col.update_one') as mock_update_one:
            mock_find_one.return_value = mock_attendee
            mock_update_one.return_value = mock.MagicMock(modified_count=1)
            response = self.app.put('/api/attendees/1', json=updated_mock_attendee)
            response2 = self.app.get('/api/attendees/1')
            self.assertEqual(response2.json['name'], "Bùi Minh Sơn")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'msg': 'User Update Successfully'})
            mock_find_one.assert_called_once_with({'STT': mock_attendee["STT"]})
            mock_update_one.assert_called_once_with({'STT': mock_attendee["STT"]},
                                                    {'$set': 
                                                        {
                                                        'STT': updated_mock_attendee['id'], 
                                                        'Họ và tên': updated_mock_attendee['name'], 
                                                        'Năm sinh': updated_mock_attendee['birth'],
                                                        'Giới tính': updated_mock_attendee['sex'], 
                                                        'Trường': updated_mock_attendee['university'], 
                                                        'Chuyên ngành': updated_mock_attendee['major']
                                                        }})


if __name__ == '__main__':
    unittest.main()

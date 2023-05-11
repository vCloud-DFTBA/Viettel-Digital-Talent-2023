import unittest
import requests
from bson import ObjectId
import json

URL_GET_ATTENDEE_BY_ID = "http://localhost:5000/getone"
URL_COMMON = "http://localhost:5000"

class TestAttendeeAPI(unittest.TestCase):
   
    def setUp(self):
        data = {
            "fullName": "NTLiinhh-general",
            "doB": "2002",
            "gender": "Male",
            "school": "University of Science and Technology",
            "major": "Global ICT"
        }
        response = requests.post(URL_COMMON, json=data)
        self._id = response.text.replace('\n', '')
        self._id = self._id.replace('"', '')
        self.assertEqual(response.status_code, 200)
   
    def test_post_attendee(self):
        data = {
            "fullName": "NTLiinhh test post",
            "doB": "2002",
            "gender": "Male",
            "school": "University of Science and Technology",
            "major": "Global ICT"
        }
        response = requests.post(URL_COMMON, json=data)
        self.assertEqual(response.status_code, 200)
    
    def test_get_all_attendees(self):
        response = requests.get(URL_COMMON)
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.json()), 0)
        
    def test_put_attendee(self):
        data = {
            "fullName": "NTLiinhh-updated",
            "doB": "2002",
            "gender": "Male",
            "school": "University of Science and Technology",
            "major": "Global ICT"
        }
        response = requests.put(f"{URL_COMMON}/{self._id}",json=data)
        self.assertEqual(response.status_code, 200)
 
    def test_get_one_attendee_by_id(self):
        response = requests.get(f"{URL_GET_ATTENDEE_BY_ID}/{self._id}")
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.json()), 0)
    
    def test_delete_attendee(self):
        response = requests.delete(f"{URL_COMMON}/{self._id}")
        self.assertEqual(response.status_code, 200)
   
    


    
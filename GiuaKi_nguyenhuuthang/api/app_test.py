import unittest
import requests
import time
from flask import jsonify
API_URL = "http://127.0.0.1:5000/api/"
class TestApp(unittest.TestCase):

    def test_insert_data_api(self):
        data = {
            "STT": "200",
            "Name": "test",
            "Year": "2000",
            "Sex": "Male",
            "School": "test",
            "Major": "test"
        }
        response = requests.post(f"http://127.0.0.1:5000/api/addstudent", json=data)

        responseJson = response.json()

        self.assertEqual(response.status_code, 200)
        

    if test_insert_data_api:
        def test_update_data_api(self):
            data = {
                "STT": "100",
                "Name": "test_update",
                "Year": "2001",
                "Sex": "Male",
                "School": "test_update",
                "Major": "test_update"
            }
            response = requests.put("http://127.0.0.1:5000/api/updatestudent/647047404e1e4bba0806aab0", json=data)
            responseJson = response.json()

            self.assertEqual(response.status_code, 200)


    if test_update_data_api:
        def test_read_data_api(self):
            response = requests.get("http://127.0.0.1:5000/api/getstudent?STT=15")

            self.assertEqual(response.status_code, 200)

    if test_read_data_api:
        def test_delete_data_api(self):
            response = requests.delete("http://127.0.0.1:5000/api/deletestudent/647047404e1e4bba0806aab0")
            self.assertEqual(response.status_code, 200)
            

if __name__ == '__main__':
    unittest.main()
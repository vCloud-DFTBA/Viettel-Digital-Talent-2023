import unittest
import requests
import time
API_URL = "http://localhost:80/api"
class TestApp(unittest.TestCase):

    def test_insert_data_api(self):
        data = {
            "id": "100",
            "name": "chungngoc",
            "username": "chungnn",
            "birth": "2002",
            "sex": "Male",
            "university": "PTIT",
            "major": "dtvt"
        }
        response = requests.post(f"{API_URL}/create/", json=data)

        responseJson = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(responseJson["id"], "100")
        requests.get("http://localhost:80/api/delete/100")

    def test_update_data_api(self):
        data = {
            "id": "100",
            "name": "chungngoc",
            "username": "chungnn",
            "birth": "2002",
            "sex": "Male",
            "university": "PTIT",
            "major": "dtvt"
        }
        response = requests.post("http://localhost:80/api/update/", json=data)
        responseJson = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(responseJson["id"], "100")

    def test_read_data_api(self):
        response = requests.get("http://localhost:80/api/read/15")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]['id'], '15')

    def test_delete_data_api(self):
        response = requests.get("http://localhost:80/api/delete/0")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Delete successfully")

if __name__ == '__main__':
    unittest.main()

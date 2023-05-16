import unittest
import requests


class TestApp(unittest.TestCase):

    # Test web page.
    def test_home_web_page(self):
        response = requests.get("http://localhost/")
        self.assertEqual(response.status_code, 200)
    def test_add_internee_web_page(self):
        response = requests.get("http://localhost/create.html")
        self.assertEqual(response.status_code, 200)
    def test_update_internee_web_page(self):
        response = requests.get("http://localhost/update.html")
        self.assertEqual(response.status_code, 200)


    # Test api.
    def test_insert_data_api(self):
        data = {
            "id": "100",
            "name": "toideptrai",
            "username": "pvt",
            "birth": "2002",
            "sex": "Male",
            "university": "PTIT",
            "major": "phu ho"
        }
        response = requests.post("http://localhost/api/create/", json=data)

        responseJson = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(responseJson["id"], "100")

        requests.get("http://localhost/api/delete/100")

    def test_update_data_api(self):
        data = {
            "id": "100",
            "name": "toideptrai",
            "username": "pvt",
            "birth": "2002",
            "sex": "Male",
            "university": "PTIT",
            "major": "phu ho"
        }
        response = requests.post("http://localhost/api/update/", json=data)

        responseJson = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(responseJson["id"], "100")

    def test_read_data_api(self):
        response = requests.get("http://localhost/api/read/29")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]['id'], '29')

    def test_delete_data_api(self):
        response = requests.get("http://localhost/api/delete/0")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "<h1 style='text-align:center; color: blue'>Delete succesfully. Reload the home page to see the differences!</h1>")

if __name__ == '__main__':
    unittest.main()

import unittest
import json
from unittest import mock

import requests


class AppTestCase(unittest.TestCase):
    @mock.patch('requests.post')
    def test_Add(self, mock_post):
        mock_post.return_value.status_code = 201

        data = {
            "id": "1",
            "name": "Nguyen Van A",
            "username": "ANV",
            "birth": 1990,
            "sex": "Male",
            "university": "ABC University",
            "major": "Computer Science"
        }

        response = requests.post("http://localhost:80/Add", json=data)

        self.assertEqual(response.status_code, 201)
        mock_post.assert_called_once_with("http://localhost:80/Add", json=data)

    @mock.patch('requests.delete')
    def test_Delete(self, mock_delete):
        mock_delete.return_value.status_code = 200

        response = requests.delete("http://localhost:80/Delete/1")

        self.assertEqual(response.status_code, 200)
        mock_delete.assert_called_once_with("http://localhost:80/Delete/1")

    @mock.patch('requests.post')
    def test_Update(self,mock_post):
        mock_post.return_value.status_code = 200

        data = {
            "name": "Jane Doe",
            "username": "janedoe",
            "birth": 1991,
            "sex": "Female",
            "university": "XYZ University",
            "major": "Data Science"
        }

        response = requests.post("http://localhost:80/Update/1", json=data)

        self.assertEqual(response.status_code, 200)
        mock_post.assert_called_once_with("http://localhost:80/Update/1", json=data)

    def test_get_all_attendees(self):
        response = requests.get("http://localhost:80/list")
        self.assertEqual(response.status_code, 200)

    def test_View(self):
        data = {
            "id": "1",
            "name": "Nguyen Van A",
            "username": "ANV",
            "birth": 1990,
            "sex": "Male",
            "university": "ABC University",
            "major": "Computer Science"
        }
        requests.post("http://localhost:80/Add", json=data)

        response = requests.get("http://localhost:80/View/1")
        self.assertEqual(response.status_code, 200)

        student = json.loads(response.text)[0]
        self.assertEqual(student["id"], "1")
        self.assertEqual(student["name"], "Nguyen Van A")
        self.assertEqual(student["username"],"ANV")
        self.assertEqual(student["birth"], 1990)
        self.assertEqual(student["sex"], "Male")
        self.assertEqual(student["university"], "ABC University")
        self.assertEqual(student["major"], "Computer Science")


if __name__ == '__main__':
    unittest.main()
from flask import Flask
import unittest
import pymongo
import requests


class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://localhost"

    def test_index(self):
        response = requests.get(self.base_url)
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        response = requests.post(f'{self.base_url}/create', data={
            "stt": "100",
            "hovaten": "testcreate",
            "username": "test",
            "namsinh": "2002",
            "gioitinh": "Nam",
            "truong": "test school",
            "chuyennganh": "test major"
        })
        self.assertEqual(response.status_code, 200)


    def test_get(self):
        response = requests.get(f'{self.base_url}/get/1')
        self.assertEqual(response.status_code, 200)

    def test_update(self):
        response = requests.post(f'{self.base_url}/update/5', data={
            "stt": "5",
            "hovaten": "testupdate",
            "username": "test",
            "namsinh": "2002",
            "gioitinh": "Nam",
            "truong": "test school",
            "chuyennganh": "test major"
        })
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        response = requests.delete(f'{self.base_url}/delete/2')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()




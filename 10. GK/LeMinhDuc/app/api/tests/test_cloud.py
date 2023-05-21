import unittest
from unittest.mock import patch

import src.db
from mongomock import MongoClient
from src import create_app


class PyMongoMock(MongoClient):
    def init_app(self, app):
        return super().__init__()


class TestCloud(unittest.TestCase):
    def test_create(self):
        request = {
            "birth_year": 2002,
            "full_name": "hacker123",
            "gender": "Nam",
            "major": "ICT",
            "university": "HUST",
            "username": "hacker123",
        }

        invalid_request = {
            "birth_year": "l33t",
            "full_name": "hacker456",
            "gender": "Nam",
            "major": "ICT",
            "university": "HUST",
            "username": "hacker456",
        }

        with patch.object(src.db, "mongo", PyMongoMock()):
            app = create_app({"MONGO_URI": ""})
            client = app.test_client()

            response = client.post("/cloud", json=invalid_request)
            self.assertEqual(response.status_code, 400)

            response = client.post("/cloud", json=request)
            self.assertEqual(response.status_code, 201)
            self.assertIsInstance(response.json, dict)
            self.assertEqual(len(response.json), len(request) + 1)
            self.assertEqual(response.json["username"], request["username"])

    def test_getAll(self):
        requests = [
            {
                "birth_year": 2002,
                "full_name": "hacker123",
                "gender": "Nam",
                "major": "ICT",
                "university": "HUST",
                "username": "hacker123",
            },
            {
                "birth_year": 2002,
                "full_name": "hacker456",
                "gender": "Nam",
                "major": "ICT",
                "university": "HUST",
                "username": "hacker456",
            },
        ]

        with patch.object(src.db, "mongo", PyMongoMock()):
            app = create_app({"MONGO_URI": ""})
            client = app.test_client()

            response = client.get("/cloud")
            self.assertEqual(response.status_code, 200)
            self.assertIsInstance(response.json, list)
            self.assertEqual(len(response.json), 0)

            for request in requests:
                client.post("/cloud", json=request)
            response = client.get("/cloud")
            self.assertEqual(response.status_code, 200)
            self.assertIsInstance(response.json, list)
            self.assertEqual(len(response.json), len(requests))

    def test_getOne(self):
        request = {
            "birth_year": 2002,
            "full_name": "hacker123",
            "gender": "Nam",
            "major": "ICT",
            "university": "HUST",
            "username": "hacker123",
        }

        with patch.object(src.db, "mongo", PyMongoMock()):
            app = create_app({"MONGO_URI": ""})
            client = app.test_client()

            response1 = client.get("/cloud/1")
            response2 = client.post("/cloud", json=request)
            response3 = client.get("/cloud/1")
            self.assertEqual(response1.status_code, 404)
            self.assertEqual(response3.status_code, 200)
            self.assertIsInstance(response3.json, dict)
            self.assertEqual(len(response3.json), len(response2.json))
            self.assertEqual(
                set(response3.json.keys()),
                set(response2.json.keys()),
            )
            for key in response3.json.keys():
                self.assertEqual(response3.json[key], response2.json[key])

    def test_update(self):
        request = {
            "birth_year": 2002,
            "full_name": "hacker123",
            "gender": "Nam",
            "major": "ICT",
            "university": "HUST",
            "username": "hacker123",
        }

        invalid_request = {
            "birth_year": "l33t",
            "full_name": "hacker456",
            "gender": "Nam",
            "major": "ICT",
            "university": "HUST",
            "username": "hacker456",
        }

        with patch.object(src.db, "mongo", PyMongoMock()):
            app = create_app({"MONGO_URI": ""})
            client = app.test_client()

            response = client.patch("/cloud/1", json=invalid_request)
            self.assertEqual(response.status_code, 400)

            response1 = client.patch("/cloud/1", json={"full_name": "bitcoins"})
            client.post("/cloud", json=request)
            response2 = client.patch("/cloud/1", json={"full_name": "bitcoins"})
            response3 = client.get("/cloud/1")
            self.assertEqual(response1.status_code, 404)
            self.assertEqual(response3.status_code, 200)
            self.assertIsInstance(response3.json, dict)
            self.assertEqual(response3.json["full_name"], "bitcoins")
            self.assertEqual(len(response3.json), len(response2.json))
            self.assertEqual(
                set(response3.json.keys()),
                set(response2.json.keys()),
            )
            for key in response3.json.keys():
                self.assertEqual(response3.json[key], response2.json[key])

    def test_remove(self):
        request = {
            "birth_year": 2002,
            "full_name": "hacker123",
            "gender": "Nam",
            "major": "ICT",
            "university": "HUST",
            "username": "hacker123",
        }

        with patch.object(src.db, "mongo", PyMongoMock()):
            app = create_app({"MONGO_URI": ""})
            client = app.test_client()

            response1 = client.delete("/cloud/1")
            client.post("/cloud", json=request)
            response2 = client.delete("/cloud/1")
            response3 = client.get("/cloud/1")
            self.assertEqual(response1.status_code, 404)
            self.assertEqual(response2.status_code, 200)
            self.assertEqual(response3.status_code, 404)

import unittest
from unittest.mock import patch, MagicMock
from unittest import mock
import app
from app.init_database import interns_data, init_db


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.create_app().test_client()
        self.app.post("/interns/delete_all")
        init_db()

    def test_test_page(self):
        response = self.app.get("/test")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Hello world")

    @mock.patch("app.create_app")
    def test_identity(self, mock_create_app):
        mock_create_app.return_value = self.app
        response = self.app.get("/identity")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"identity": "127.0.0.1"})

    @patch("pymongo.collection.Collection.find")
    def test_getAllAttendees(self, mock_find):
        mock_cursor = MagicMock()
        mock_cursor.sort.return_value = mock_cursor
        mock_cursor.__iter__.return_value = [
            {
                "_id": "645bec7f8022f1a858e69c42",
                "email": "sonbm@is.viettel.com.vn",
                "name": "Bùi Minh Sơn",
                "university": "Đại học Công nghệ - Đại học Quốc gia Hà Nội",
                "year_of_birth": "2002",
            },
            {
                "_id": "645bec7f8022f1a858e69c61",
                "email": "duongtm@is.viettel.com.vn",
                "name": "Trần Minh Dương",
                "university": "Đại học Công nghệ - Đại học Quốc gia Hà Nội",
                "year_of_birth": "2002",
            },
        ]
        mock_find.return_value = mock_cursor
        response = self.app.get("/interns")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["name"], "Bùi Minh Sơn")
        self.assertEqual(data[1]["name"], "Trần Minh Dương")

    def test_get_all_interns(self):
        response = self.app.get("/interns")
        self.test_id = response.json[0]["id"]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), len(interns_data))
        for i in range(len(response.json)):
            self.assertEqual(response.json[i]["name"], interns_data[i]["name"])
            self.assertEqual(
                response.json[i]["university"], interns_data[i]["university"]
            )
            self.assertEqual(
                response.json[i]["year_of_birth"], interns_data[i]["year_of_birth"]
            )

    def test_get_intern_by_id(self):
        response = self.app.get("/interns")
        self.assertEqual(response.status_code, 200)
        first_id = response.json[0]["id"]
        response = self.app.get(f"/interns/{first_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["name"], interns_data[0]["name"])
        self.assertEqual(response.json["university"], interns_data[0]["university"])
        self.assertEqual(
            response.json["year_of_birth"], interns_data[0]["year_of_birth"]
        )

    def test_get_intern_by_id_not_found(self):
        response = self.app.get("/interns")
        self.assertEqual(response.status_code, 200)
        first_id = response.json[0]["id"]
        response = self.app.get(f"/interns/{first_id}1")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json["message"], "Get failed")

    def test_create_intern(self):
        response = self.app.get("/interns")
        self.assertEqual(response.status_code, 200)
        length = len(response.json)
        response = self.app.post(
            "/interns",
            json={
                "name": "Nguyen Dinh Minh",
                "university": "Dai hoc Cong nghe - DHQGHN",
                "year_of_birth": "2010",
            },
        )
        self.assertEqual(response.status_code, 200)
        response = self.app.get("/interns")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), length + 1)

    def test_update_intern_by_id(self):
        response = self.app.get("/interns")
        self.assertEqual(response.status_code, 200)
        first_id = response.json[1]["id"]
        response = self.app.put(
            f"/interns/{first_id}",
            json={
                "name": "Nguyen Van A",
                "university": "Dai hoc Cong nghe",
                "year_of_birth": "2000",
            },
        )
        self.assertEqual(response.status_code, 200)
        response = self.app.get(f"/interns/{first_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["name"], "Nguyen Van A")

    def test_delete_intern_by_id(self):
        response = self.app.get("/interns")
        self.assertEqual(response.status_code, 200)
        first_id = response.json[1]["id"]
        response = self.app.post(
            f"/interns/delete_many",
            json={
                "ids": [first_id],
            },
        )
        self.assertEqual(response.status_code, 200)
        response = self.app.get(f"/interns/{first_id}")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json["message"], "Get failed")

    def test_delete_intern_by_id_not_found(self):
        response = self.app.get("/interns")
        self.assertEqual(response.status_code, 200)
        first_id = response.json[1]["id"]
        response = self.app.post(
            f"/interns/delete_many",
            json={
                "ids": [first_id],
            },
        )
        self.assertEqual(response.status_code, 200)
        response = self.app.get(f"/interns/{first_id}")
        self.assertEqual(response.status_code, 400)

    def test_delete_all_interns(self):
        response = self.app.get("/interns")
        self.assertEqual(response.status_code, 200)
        response = self.app.post("/interns/delete_all")
        self.assertEqual(response.status_code, 200)
        response = self.app.get("/interns")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 0)

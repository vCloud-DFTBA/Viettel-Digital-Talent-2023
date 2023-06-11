# importing sys
from bson.objectid import ObjectId
from Flask_CRUD.app import create_app
import unittest
import mongomock


def mockdatabase():
    clientMongo = mongomock.MongoClient()
    db = clientMongo["mydatabase"]
    collection = db["mycollection"]
    collection.insert_one(
        {
            "full_name": "Init student",
            "birth_year": "1945",
            "major": "AI",
            "unversity": "ITMO",
            "gender": "Nam",
        }
    )
    return collection


class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.db = mockdatabase()
        self.app = create_app(self.db)
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()
        self.init_data = self.db.find_one({})
        self.test_data = {
            "full_name": "Test student",
            "birth_year": "1975",
            "major": "ML",
            "unversity": "ITMO",
            "gender": "Nữ",
        }

    def tearDown(self):
        # Restart database
        self.db.drop()

    def test_index(self):
        # Check home page
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_add_student(self):
        # Test add student
        response = self.client.post("/action_add", data=self.test_data)
        self.assertEqual(response.status_code, 302)
        result = self.db.find_one({"full_name": "Test student"})
        self.assertIsNotNone(result)
        self.assertEqual(result["birth_year"], "1975")
        self.assertEqual(result["major"], "ML")
        self.assertEqual(result["unversity"], "ITMO")
        self.assertEqual(result["gender"], "Nữ")

    def test_remove_student(self):
        # Test remove student
        response = self.client.delete("/remove", data={"_id": self.init_data["_id"]})
        self.assertEqual(response.status_code, 302)

        removed_student = self.db.find_one({"_id": self.init_data["_id"]})
        self.assertEqual(removed_student, None)

    def test_update(self):
        # Test redirice to page update student
        response = self.client.get(f'/update?_id={str(self.init_data["_id"])}')
        self.assertEqual(response.status_code, 200)

    def test_action_update(self):
        # Test update info student
        url = f"/action_update?_id={str(self.init_data['_id'])}"
        response = self.client.post(url, data=self.test_data)
        assert response.status_code == 302

        # Verify the update was successful
        updated_student = self.db.find_one({"_id": ObjectId(self.init_data["_id"])})
        self.assertIsNotNone(updated_student)
        assert updated_student["birth_year"] == "1975"


if __name__ == "__main__":
    unittest.main()

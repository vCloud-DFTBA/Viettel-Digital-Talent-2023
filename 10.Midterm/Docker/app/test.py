import unittest
from bson import ObjectId
import app
from app import application, db

app.mongo_uri = "mongodb://localhost:27017/VDT23"

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        application.config["TESTING"] = True
        self.app = application.test_client()

    def test_lists_route(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)

    def test_action_route(self):
        data = {
            "Name": "Test",
            "DOB": "2000",
            "Gender": "Name",
            "University": "HUST",
            "Major": "ET",
            "Username": "test"
        }
        response = self.app.post("/action", data=data)
        self.assertEqual(response.status_code, 302)

    def test_remove_route(self):
        test_doc = db.attendees.insert_one({
            "Name": "Test",
            "DOB": "2000",
            "Gender": "Name",
            "University": "HUST",
            "Major": "ET",
            "Username": "test"
        })
        response = self.app.get(f"/remove?key={test_doc.inserted_id}")
        self.assertEqual(response.status_code, 302)

    def test_update_route(self):
        test_doc = db.attendees.insert_one({
            "Name": "Test",
            "DOB": "2000",
            "Gender": "Name",
            "University": "HUST",
            "Major": "ET",
            "Username": "test"
        })
        response = self.app.get(f"/update?key={test_doc.inserted_id}")
        self.assertEqual(response.status_code, 200)

    def test_action3_route(self):
        test_doc = db.attendees.insert_one({
            "Name": "Test",
            "DOB": "2000",
            "Gender": "Name",
            "University": "HUST",
            "Major": "ET",
            "Username": "test"
        })
        data = {
            "_id": str(test_doc.inserted_id),
            "Name": "Updated Test",
            "DOB": "2000",
            "Gender": "Name",
            "University": "HUST",
            "Major": "ET",
            "Username": "test"
        }
        response = self.app.post("/action3", data=data)
        self.assertEqual(response.status_code, 302)
        updated_doc = db.attendees.find_one({"_id": ObjectId(test_doc.inserted_id)})
        self.assertEqual(updated_doc["Name"], "Updated Test")

if __name__ == "__main__":
    unittest.main()

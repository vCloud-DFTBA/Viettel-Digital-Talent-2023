from flask import Flask
import logging
import unittest
from app import app


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_post_student(self):
        logging.info("Start the post student test")
        response = self.app.get("/list")
        assert response.status_code == 200
        assert response.json() != None



if __name__ == "__main__":
    unittest.main()

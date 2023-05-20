
import unittest

from bson import ObjectId
from services.buddy_service import BuddySerivce
import os
import pymongo
from database.seed import seed_data



class BuddyServiceTest(unittest.TestCase):

    
    @classmethod
    def setUpClass(cls) -> None:
        _database_name = "uniitest_service"
        DB_URI_TEST = os.getenv("DB_URI_TEST", "mongodb://localhost:27018/")
        db_client = pymongo.MongoClient(DB_URI_TEST)
        db = db_client[_database_name]
        cls.buddies_test_collection = db["buddies_test"]
        # db_client.drop_database[_database_name]
        cls.buddy_service = BuddySerivce(cls.buddies_test_collection)
        
        cls.buddy_test_dict = {
            "name":"VDT",
            "university":"VDT",
            "gender":"nam",
            "yearOfBirth":"2001",
            "major":"Cloud"
        } 
    
    def setUp(self):
        # seed data before running test
        seed_data(self.buddies_test_collection)

    def tearDown(self):
        # remove all data after running a test
        self.buddies_test_collection.delete_many({})
        return
    
    def test_get_buddy_service_returns_a_list(self):
        result = self.buddy_service.get_buddies()
        self.assertIsInstance(result, list,"returned object from get_buddies() is a list")
        
    def test_get_a_buddy_service_returns_a_buddy(self):
        buddy_0 = self.buddies_test_collection.find({})[0]
        test_buddy0 = self.buddy_service.get_buddy(buddy_0["_id"])
        self.assertDictEqual(buddy_0,test_buddy0)
        
    def test_get_a_buddy_raise_exception_with_incorrect_id(self):
        incorrect_buddy_id = "incorrect_buddy_id"
        self.assertRaises(RuntimeError,lambda: self.buddy_service.get_buddy(incorrect_buddy_id))   
    
    def test_add_a_buddy_success(self):
        inserted_buddy = self.buddy_service.add_buddy(self.buddy_test_dict)
        inserted_buddy_in_database = self.buddies_test_collection.find_one({"_id":ObjectId(inserted_buddy["_id"])})
        self.assertEqual(inserted_buddy["_id"], str(inserted_buddy_in_database["_id"]))
    
    def test_update_a_buddy_success(self):
        buddy_0 = self.buddies_test_collection.find({})[0]
        self.buddy_service.update_buddy(buddy_0["_id"], self.buddy_test_dict)
        new_buddy_0 = self.buddies_test_collection.find_one({"_id":ObjectId(buddy_0["_id"])},{"_id": False})
        self.assertEqual(new_buddy_0,self.buddy_test_dict)
    
    def test_delete_a_buddy_success(self):
        buddy_0 = self.buddies_test_collection.find({})[0]
        self.buddy_service.delete_buddy(buddy_0["_id"])
        
        buddy_0_in_database = self.buddies_test_collection.find_one({"_id":ObjectId(buddy_0["_id"])})
        self.assertIsNone(buddy_0_in_database)
if __name__ == '__main__':
    unittest.main()
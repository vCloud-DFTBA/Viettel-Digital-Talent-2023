from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from unittest import mock
from api.views import createUser
import json
fakeUser={
    "Name": "fake",
    "Username":"fk",
    "Birthyear": "2003",
    "Gender": "Nam",
    "University": "fake fake fake university",
    "Major":"faking data"
}   
class ApiTest(TestCase):
    def setUp(self):
        # test_addUserUsingIndex(self):
        res=self.client.post('/createuser',json.dumps(fakeUser),content_type="application/json").json()
        self.assertTrue(isinstance(res["error"],bool) and not res["error"] ,"Error when adding new user.")
    def test_list_and_get(self):   
        # test_listUsers(self):
        res=self.client.get('/listusers').json()["users"]
        self.assertIn(fakeUser["Username"],[v["Username"] for v in res],"Posted user not exists in database, or there are errors in the listing function.")
        id=[v["id"] for v in res if v["Username"]==fakeUser["Username"]][0]
        self.assertTrue(id!=None)
        # test_getUser(self):
        res=self.client.get('/getuser/'+str(id)).json()
        self.assertTrue(isinstance(res["error"],bool) and not res["error"],"Error when getting user")
        self.assertEqual(fakeUser["Username"],res["user"]["Username"],"Get User: Username not match.")
    def test_update(self):
        res=self.client.post('/updateuser',json.dumps({'user':fakeUser,'update':{'Gender':'Nu'}}),content_type="application/json").json()
        self.assertTrue(isinstance(res["error"],bool) and not res["error"] ,"Error when updating user.")
    def tearDown(self):
        #test_deleteUser(self):
        res=self.client.post('/deleteuser',json.dumps({"Username":fakeUser["Username"]}),content_type="application/json").json()
        self.assertTrue(isinstance(res["error"],bool) and not res["error"] ,"Error when deleting user.")

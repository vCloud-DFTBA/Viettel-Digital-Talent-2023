from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from users.views import index,AddForm
class WebPageTest(TestCase):
    def test_indexMapping(self):
        res=self.client.get('/')
        self.assertTemplateUsed(response,'index.html')
    def test_addUserUsingIndex(self):
        fakeUser={
            "Name": "fake",
            "Username":"fk",
            "Birthyear": "2003",
            "Gender": "Nam",
            "University": "fake fake fake university",
            "Major":"faking data"
        }   
        self.fail("Finish the test")
        res=self.client.post('/',fakeUser)
        rows=self.browser.find_element_by_id('userTable').find_elements_by_tag_name('tr')
        self.assertIn()

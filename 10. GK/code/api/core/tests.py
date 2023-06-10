from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Attendee
from .serializers import AttendeeSerializer
# Create your tests here.




class TestAttendee(APITestCase):
    @classmethod
    def setUpTestData(cls):
        Attendee.objects.create(full_name="123",username="asasd",gender="Nam",DoB="2023",university_name="hust",major="ict")

    def test_get_all_datas(self):
        path = reverse('attendee-list')
        res = self.client.get(path=path)
        self.assertEquals(res.status_code, status.HTTP_200_OK)

    def test_post_data(self):
        path = reverse('attendee-list')
        data_post = {
            "full_name": "abc",
            "username": "asdasdasd",
            "gender": "Nữ",
            "DoB": "2023",
            "university_name": "hust",
            "major": "ict"
        }
        res = self.client.post(path=path, data=data_post, format='json')
        self.assertEquals(res.status_code, status.HTTP_201_CREATED)

    def test_get_spec_data(self):
        path = reverse("attendee-detail", kwargs={"pk": 1})
        res = self.client.get(path)
        self.assertEquals(res.status_code, status.HTTP_200_OK)

    def test_put_spec_data(self):
        path = reverse("attendee-detail", kwargs={"pk": 1})
        data_put = {
            "full_name": "abc",
            "username": "asdasdasd",
            "gender": "Nữ",
            "DoB": "2023",
            "university_name": "hust",
            "major": "ict"
        }
        res = self.client.put(path,data=data_put)
        self.assertEquals(res.status_code,status.HTTP_200_OK)

    def test_patch_spec_data(self):
        path = reverse("attendee-detail", kwargs={"pk": 1})
        data_put = {
            "full_name": "cef",
            "university_name": "ptit",
            "major": "ict"
        }
        res = self.client.patch(path, data=data_put, format='json')
        self.assertEquals(res.status_code, status.HTTP_200_OK)

    def test_delete_spec_data(self):
        path = reverse("attendee-detail", kwargs={"pk": 1})
        res = self.client.delete(path)
        self.assertEquals(res.status_code, status.HTTP_204_NO_CONTENT)

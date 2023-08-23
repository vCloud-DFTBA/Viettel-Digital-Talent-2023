from django.urls import path,include
from .views import AttendeeViewset
from rest_framework.routers import DefaultRouter
# import pprint
route = DefaultRouter()
route.register("Attendees", AttendeeViewset, basename="attendee")

# pprint.pprint(route.get_urls())

urlpatterns = [
    path("", include(route.urls))
]

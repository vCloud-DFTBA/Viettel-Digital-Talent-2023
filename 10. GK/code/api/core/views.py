from rest_framework import status, viewsets, permissions
from .models import Attendee
from .serializers import AttendeeSerializer
# Create your views here.


class AttendeeViewset(viewsets.ModelViewSet):
    queryset = Attendee.objects.all()
    serializer_class = AttendeeSerializer
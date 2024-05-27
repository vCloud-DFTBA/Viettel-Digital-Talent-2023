from rest_framework import serializers
from .models import Attendees

class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendees
        fiels = ["__all__"]
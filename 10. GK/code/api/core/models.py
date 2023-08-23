from django.db import models
from datetime import date


# Create your models here.
class Attendee(models.Model):
    default_year = date.today().year
    GENDER_MALE = "Nam"
    GENDER_FEMALE = "Nữ"
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100, null=False, blank=False)
    username = models.CharField(max_length=20, null=True, blank=False)
    gender = models.TextField(choices=GENDER_CHOICES, default=0)
    DoB = models.TextField(default=str(default_year))
    university_name = models.CharField(max_length=200, null=True)
    major = models.TextField(default="NULL")

    def __str__(self):
        return self.full_name

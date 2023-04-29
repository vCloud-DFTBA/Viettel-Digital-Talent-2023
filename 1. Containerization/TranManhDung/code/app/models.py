from django.db import models

# Create your models here.
class Attendees(models.Model):
    GENDER_MALE = "Nam"
    GENDER_FEMALE = "Nữ"
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    gender = models.TextField(choices=GENDER_CHOICES, default=0)
    DoB = models.DateField(null=True)
    university_name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
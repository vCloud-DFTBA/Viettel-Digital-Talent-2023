from django.shortcuts import render,HttpResponse
from .models import Attendees
from .serializers import AttendeeSerializer
# Create your views here.
def index(request):
    data_query = Attendees.objects.all()
    return render(request, "app/index.html", {"datas": data_query})
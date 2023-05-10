from django.shortcuts import render
# from django.forms.renders import TemplatesSetting
from django import forms
import pymongo

class AddForm(forms.Form):
    name=forms.CharField()
    birthyear=forms.CharField()
    gender=forms.CharField()
    university=forms.CharField()
    major=forms.CharField()

def index(request):
    client = pymongo.MongoClient("mongodb://db:27017/",serverSelectionTimeoutMS=10)
    client.server_info()
    if request.method=='POST':
        form=AddForm(request.POST)
        if(form.is_valid()):
            client['data']['users'].insert_one({'Name':form.cleaned_data['name'],'Birthyear':form.cleaned_data['birthyear'],'Gender':form.cleaned_data['gender'],'University':form.cleaned_data['university'],'Major':form.cleaned_data['major']})
    cursor=client["data"]["users"].find()
    userData=[]
    for d in cursor: 
        userData.append([d['Name'],d['Birthyear'],d['Gender'],d['University'],d['Major']])
    return render(request,'index.html',{"userData":userData,"addForm":AddForm()})

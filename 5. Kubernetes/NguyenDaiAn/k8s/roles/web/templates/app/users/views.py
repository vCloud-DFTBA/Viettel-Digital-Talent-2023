from django.shortcuts import render,redirect
from django.http import JsonResponse
# from django.forms.renders import TemplatesSetting
from django import forms
import pymongo
import json
import requests
from bson.objectid import ObjectId
def _getUserTable():
    client = pymongo.MongoClient("mongodb://db-service:27017",serverSelectionTimeoutMS=60)
    client.server_info()
    return client["data"]["users"]
class AddForm(forms.Form):
    Name=forms.CharField()
    Username=forms.CharField()
    Birthyear=forms.CharField()
    Gender=forms.CharField()
    University=forms.CharField()
    Major=forms.CharField()
def index(request):
    client = pymongo.MongoClient("mongodb://db-service:27017/",serverSelectionTimeoutMS=10)
    client.server_info()
    if request!=None and request.method=='POST':
        form=AddForm(request.POST)
        if(form.is_valid()):
            client['data']['users'].insert_one({'Name':form.cleaned_data['Name'],'Username':form.cleaned_data['Username'],'Birthyear':form.cleaned_data['Birthyear'],'Gender':form.cleaned_data['Gender'],'University':form.cleaned_data['University'],'Major':form.cleaned_data['Major']})
    cursor=list(client["data"]["users"].find())
    for i in cursor:
        i['id']=i['_id']
    return render(request,'index.html',{"userData":cursor,"addForm":AddForm()})
def deleteUser(req,id):
    client = pymongo.MongoClient("mongodb://db-service:27017/",serverSelectionTimeoutMS=10)
    client.server_info()
    client["data"]["users"].delete_one({'_id':ObjectId(id)})
    return redirect("index")
class UserForm(forms.Form):
    Name=forms.CharField(required=False)
    Username=forms.CharField(required=False)
    Birthyear=forms.CharField( required=False)
    Gender=forms.CharField(required=False)
    University=forms.CharField(required=False)
    Major=forms.CharField( required=False)
def updateUser(req,id):
    _filter={'_id':ObjectId(id)}
    error=True
    if(req.method=='POST'):
        form=UserForm(req.POST)
        if form.is_valid():
            user=dict()
            for k,v in form.cleaned_data.items():
                if v:
                    user[k]=v
            updated=_getUserTable().update_one(_filter,{"$set":user}).modified_count
            if updated==1:
                return redirect("index")
    else:
        error=False
    old_user= _getUserTable().find_one(_filter)
    del old_user['_id']
    return render(req,'update_user.html',{"updateForm":UserForm(),"error":error,"id":id,"userData":[old_user]})


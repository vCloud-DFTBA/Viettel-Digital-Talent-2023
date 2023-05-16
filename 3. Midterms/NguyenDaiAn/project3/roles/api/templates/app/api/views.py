from django.shortcuts import render,redirect
from django.http import JsonResponse
import pymongo
import json
from bson.objectid import ObjectId
from django.views.decorators.csrf import csrf_exempt

def _getUserTable():
    client = pymongo.MongoClient("mongodb://db:27017",serverSelectionTimeoutMS=10)
    client.server_info()
    return client["data"]["users"]
def listUsers(req):
    tb=_getUserTable()
    users=[]
    cursor= tb.find()
    for i in cursor:
        users.append({'Name':i['Name'],'Username':i['Username'],'id':str(i['_id'])});
    return JsonResponse({'users':users})
def getUser(req,id):
    error=True
    user=None
    try:
      if(id):
          user=_getUserTable().find_one({'_id':ObjectId(id)})
          if(user):
              error=False
              user['id']=id
              del user['_id']
    finally:
        return JsonResponse({'user':user,'error':error})
@csrf_exempt
def createUser(req):
    error=True
    user=None
    body=None
    try:
        if(req.method=='POST'):
            body_unicode = req.body.decode('utf-8')
            body = json.loads(body_unicode)
            error=False
            _getUserTable().insert_one(body)
            user=body
            if(user):
                error=False
                user['id']=str(user['_id'])
                del user['_id']
    finally:
        return JsonResponse({'user':user,'error':error})
    return JsonResponse({'user':user,'error':error})
@csrf_exempt
def updateUser(req):
    error=True
    updated=0
    body=None
    try:
        if(req.method=='POST'):
            body_unicode = req.body.decode('utf-8')
            body = json.loads(body_unicode)
            updated=_getUserTable().update_one(body["user"],{"$set":body["update"]}).modified_count
            error=False
    finally:
        return JsonResponse({'updated':updated,'error':error})
@csrf_exempt
def deleteUser(req):
    error=True
    updated=0
    body=None
    try:
        if(req.method=='POST'):
            body_unicode = req.body.decode('utf-8')
            body = json.loads(body_unicode)
            updated=_getUserTable().delete_one(body).deleted_count
            error=False
    finally:
        return JsonResponse({'updated':updated,'error':error})

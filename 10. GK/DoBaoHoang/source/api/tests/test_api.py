import requests
import random
from pymongo import MongoClient
from bson import ObjectId

base_url = 'http://localhost:8080/api'
MONGODB_DATABASE = "flaskdb"

client = MongoClient(f"localhost:27017")
db = client[MONGODB_DATABASE]
collection = db.attendees

def is_in(user, user_list):
    # nếu có user thì user phải có trong list
    for u in user_list:
        if user.get('name') == u.get('name'):
            return True
        
    return False

def test_list_api():
    url = base_url + '/profiles'
    response = requests.get(url)
    assert response.status_code == 200

    attendees = collection.find({})
    user_list = response.json().get('attendees')

    for attendee in attendees:
        assert is_in(attendee, user_list)

def test_read_api():
    name = random.randint(0, 9999)
    result = collection.insert_one({'name': name})

    url = base_url + f'/profile/{result.inserted_id}'
    response = requests.get(url)

    assert response.status_code == 200
    assert response.json().get('name') == name

    collection.delete_one({'name': name})

def test_create_api():
    url = base_url + '/profile/create'
    attendee = {}

    response = requests.post(url, data=attendee)

    # an attendee without name is not valid
    assert response.status_code == 400
    assert response.content == b"not a valid profile"

    attendee['name'] = random.randint(0, 9999)
    response = requests.post(url, data=attendee)

    # attendee must exist after created
    assert response.status_code == 201
    id = response.content.decode('utf-8')
    user = collection.find_one({'_id': ObjectId(id)})
    assert user != None

    collection.delete_one({'_id': ObjectId(id)})

def test_update_api():
    url = base_url + '/profile/123'
    response = requests.put(url, {})

    # user is not existed
    assert response.status_code == 404
    assert response.content.decode('utf-8') == "attendee doesn't exist"

    # make sure user is updated
    randint = random.randint(0, 9999)
    result = collection.insert_one({'name': randint})

    id = str(result.inserted_id)
    url = base_url + f'/profile/{id}'

    response = requests.put(url, {'name': 'abc', 'gender': 'nam'})

    assert response.status_code == 200
    attendee = collection.find_one({'_id': ObjectId(id)})
    assert attendee.get('name') == randint
    assert attendee.get('gender') == 'nam'

    collection.delete_one({'_id': ObjectId(id)})

def test_delete_api():
    url = base_url + '/profile/123'
    response = requests.put(url, {})

    # user is not existed
    assert response.status_code == 404
    assert response.content.decode('utf-8') == "attendee doesn't exist"

    # make sure user is deleted
    randint = random.randint(0, 9999)
    result = collection.insert_one({'name': randint})

    id = str(result.inserted_id)
    url = base_url + f'/profile/{id}'

    response = requests.delete(url)
    assert response.status_code == 200
    attendee = collection.find_one({'_id': ObjectId(id)})
    assert attendee == None
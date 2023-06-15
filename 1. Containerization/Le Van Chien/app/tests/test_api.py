import json
from project.api import create_app

GET_ALL = '/people/'
GET_BY_USERNAME = '/people/chienlv'
GET_BY_ID = '/people/11'
PUT_NEW_DATA = 'people/create/'
UPDATE_DATA = 'people/update/chienlv'
DELETE_DATA = 'people/delete/chienlv'

def test_getByUsername(db):
    app = create_app(db)
    response = app.test_client().get(GET_BY_USERNAME)
    data = json.loads(response.data.decode('utf-8'))

    assert len(data) == 1
    assert data[0]['id'] == 11
    assert response.status_code == 200

def test_getAll(db):
    app = create_app(db)
    response =  app.test_client().get(GET_ALL)
    data = json.loads(response.data.decode('utf-8'))

    assert type(data) is list
    assert type(data[0]) is dict
    assert data[10]['id'] == 11
    assert data[10] ['username'] == 'chienlv'
    assert response.status_code == 200

def test_getByID(db):
    app = create_app(db)
    response =  app.test_client().get(GET_BY_ID)
    data = json.loads(response.data.decode('utf-8'))

    assert type(data[0]) is dict
    assert len(data) == 1
    assert data[0]['username'] == 'chienlv'
    assert response.status_code == 200

def test_create(db):
    app = create_app(db)
    client = app.test_client()

    def getAll(client):
        response = client.get(GET_ALL)
        data = json.loads(response.data.decode('utf-8'))
        return data

    dataBeforePUT = getAll(client)


    newData = {
        'id': 50,
        'name': "Lorem Ipsum",
        'username': 'li',
        'yob': 2002,
        'sex': 'nam',
        'school': 'Vietnam National University',
        'major': 'School of Aerospace Engineering'
    }

    headers = {
        'Content-Type': 'application/json'
    }

    response = client.put(PUT_NEW_DATA, data=json.dumps(newData), headers=headers)


    dataAfterPUT = getAll(client)

    assert len(dataAfterPUT) == len(dataBeforePUT) + 1
    assert dataAfterPUT[-1]['id'] == 50
    assert dataAfterPUT[-1]['username'] == 'li'
    assert response.status_code == 200

def test_update(db):
    app = create_app(db)
    client = app.test_client()

    def getOne(client):
        response = client.get(GET_BY_USERNAME)
        data = json.loads(response.data.decode('utf-8'))
        return data

    dataBeforePUT = getOne(client)


    newData = {
        'school': 'Vietnam National University',
        'major': 'School of Aerospace Engineering'
    }

    headers = {
        'Content-Type': 'application/json'
    }

    response = client.put(UPDATE_DATA, data=json.dumps(newData), headers=headers)


    dataAfterPUT = getOne(client)

    assert dataAfterPUT[0]['username'] == 'chienlv'
    assert dataAfterPUT[0]['major'] == 'School of Aerospace Engineering'
    assert response.status_code == 200


def test_delete(db):
    app = create_app(db)
    client = app.test_client()

    def getAll(client):
        response = client.get(GET_ALL)
        data = json.loads(response.data.decode('utf-8'))
        return data

    dataBeforePUT = getAll(client)


    response = client.delete(DELETE_DATA)


    dataAfterPUT = getAll(client)

    assert len(dataAfterPUT) == len(dataBeforePUT) -1
    assert response.status_code == 200
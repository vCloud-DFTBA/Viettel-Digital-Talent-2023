import pytest
from flask import Flask, render_template, jsonify, request, redirect, url_for
from bson import ObjectId
import requests
import csv
from mongomock import MongoClient
from app import create_app

test_id = []
# Fixture to create the test database
@pytest.fixture(scope='session')
def test_db():
    client = MongoClient()
    db_name = "db_test"
    app, db = create_app(client, db_name)
    client = app.test_client()

    # Add test data to the database
    data = [
        {
            'Họ và tên': 'Ten 1',
            'Năm sinh': '1234',
            'Giới tính': 'gioi_tinh',
            'Trường': 'truong1',
            'Chuyên ngành': 'nganh1'
        },
        {
            'Họ và tên': 'Ten 2',
            'Năm sinh': '5678',
            'Giới tính': 'gioi_tinh',
            'Trường': 'truong2',
            'Chuyên ngành': 'nganh2'
        }
    ]
    db.mytable.insert_many(data)

    test_id.extend([str(doc["_id"]) for doc in db.mytable.find({}, {"_id": 1})])
    print("Test Database Content:",test_id) 
    # Yield the database object
    yield db

    # Teardown: remove the test data from the database
    db.mytable.delete_many({})


def test_get_info(test_db):
    app, db = create_app(test_db.client, "db_test")
    app.testing = True
    client = app.test_client()

    # Perform a GET request to '/get/<string:id>' with a valid ID
    # response = client.get(f'/get/{str(test_db.mytable.find_one()[test_id[0]])}')
    response = client.get(f'/get/{test_id[0]}')

    # Assert the response status code is 200
    assert response.status_code == 200

    # Assert the response data is in JSON format
    assert response.content_type == 'application/json'
    data = response.get_json()
    assert 'attendee' in data
    attendee = data['attendee']
    assert 'Chuyên ngành' in attendee
    assert 'Giới tính' in attendee
    assert 'Họ và tên' in attendee
    assert 'Năm sinh' in attendee
    assert 'Trường' in attendee
    assert '_id' in attendee
    assert attendee['Họ và tên'] == 'Ten 1'
    assert attendee['Năm sinh'] == '1234'
    assert attendee['Giới tính'] == 'gioi_tinh'
    assert attendee['Trường'] == 'truong1'
    assert attendee['Chuyên ngành'] == 'nganh1'
    assert attendee['_id'] == test_id[0]


def test_table_data(test_db):
    app, db = create_app(test_db.client, "db_test")
    app.testing = True
    client = app.test_client()

    # Perform a GET request to '/api/table'
    response = client.get('/api/table')

    # Assert the response status code is 200
    assert response.status_code == 200

    # Assert the response data is in JSON format
    assert response.content_type == 'application/json'
    data = response.get_json()
    assert len(data) == 2
    assert {'Họ và tên': 'Ten 1', '_id': test_id[0]} in data
    assert {'Họ và tên': 'Ten 2', '_id': test_id[1]} in data


def test_create_entry(test_db):
    app, db = create_app(test_db.client, "db_test")
    app.testing = True
    client = app.test_client()

    # Define the data to be sent in the POST request
    data = {
        'Họ và tên': 'Ten 3',
        'Năm sinh': '9012',
        'Giới tính': 'gioi_tinh',
        'Trường': 'truong3',
        'Chuyên ngành': 'nganh3'
    }

    # Perform a POST request to '/api/write_data' with the data
    response = client.post('/api/write_data', data=data)

    # Assert the response status code is 302 (redirect)
    assert response.status_code == 302

    # Assert the response redirected to '/table'
    assert response.location == '/table'

    # Check if the new entry is added to the database
    new_entry = db.mytable.find_one({'Họ và tên': 'Ten 3'})
    assert new_entry is not None
    assert new_entry['Năm sinh'] == '9012'
    assert new_entry['Giới tính'] == 'gioi_tinh'
    assert new_entry['Trường'] == 'truong3'
    assert new_entry['Chuyên ngành'] == 'nganh3'

def test_delete_entry(test_db):
    app, db = create_app(test_db.client, "db_test")
    app.testing = True
    client = app.test_client()

   # Perform a POST request to '/api/delete_entry' with the entry_name parameter
    response = client.post('/api/delete_entry', data={'entry_name': 'Ten 3'})

    # Assert the response status code is 302 (redirect)
    assert response.status_code == 302

    # Assert the response redirected to '/table'
    assert response.location == '/table'
    # Check if the entry is deleted from the database
    deleted_entry = db.mytable.find_one({'Họ và tên': 'Ten 3'})
    assert deleted_entry is None

def test_update_entry(test_db):
    app, db = create_app(test_db.client, "db_test")
    app.testing = True
    client = app.test_client()

    # Insert a test entry into the database
    test_entry = {
        'Họ và tên': 'Ten 4',
        'Năm sinh': '1234',
        'Giới tính': 'gioi_tinh',
        'Trường': 'truong4',
        'Chuyên ngành': 'nganh4'
    }
    inserted_entry = test_db.mytable.insert_one(test_entry)

    # Perform a POST request to '/api/update_entry' with the updated data
    updated_data = {
        '_id': str(inserted_entry.inserted_id),
        'ho_ten': 'Ten 4 Updated',
        'nam_sinh': '5678',
        'gioi_tinh': 'updated_gioi_tinh',
        'truong': 'updated_truong',
        'chuyen_nganh': 'updated_nganh'
    }
    response = client.post('/api/update_entry', data=updated_data)

    # Assert the response status code is 302 (redirect)
    assert response.status_code == 302

    # Assert the response redirected to '/table'
    assert response.location == '/table'

    # Check if the entry is updated in the database
    updated_entry = test_db.mytable.find_one({'_id': inserted_entry.inserted_id})
    assert updated_entry['Họ và tên'] == 'Ten 4 Updated'
    assert updated_entry['Năm sinh'] == '5678'
    assert updated_entry['Giới tính'] == 'updated_gioi_tinh'
    assert updated_entry['Trường'] == 'updated_truong'
    assert updated_entry['Chuyên ngành'] == 'updated_nganh'

if __name__ == '__main__':
    pytest.main()

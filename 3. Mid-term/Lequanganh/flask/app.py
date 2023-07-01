from flask import Flask, render_template, jsonify, request, redirect, url_for
from pymongo import MongoClient
from bson import ObjectId
import requests
import csv
import os


def create_app(client,db_name):
    app = Flask(__name__)
    db = client[db_name]

    @app.route('/hello')
    def index():
        client_info = str(client)
        db_info = str(db)
        return jsonify({'client': client_info, 'database': db_info})


    @app.route('/')
    def display_table():
        # Send POST request to 'localhost:5000/create_database_api'
        create_database_url = 'http://localhost:5000/api/create-database'
        create_response = requests.post(create_database_url)

        if create_response.status_code == 200:
            # Send GET request to 'localhost:5000/table_data'
            table_data_url = 'http://localhost:5000/api/table'
            table_data_response = requests.get(table_data_url)

            if table_data_response.status_code == 200:
                data = table_data_response.json()
                return render_template('table.html', data=data,header_color=os.environ['COLOR'])
            else:
                # Handle failed GET request to 'localhost:5000/table_data'
                return f'Failed to fetch table data. Status code: {table_data_response.status_code}'
        else:
            # Handle failed POST request to 'localhost:5000/create_database_api'
            return f'Failed to create database. Status code: {create_response.status_code}'


    @app.route('/profile/<attendee_id>')
    def profile(attendee_id):
        attendee_info = db.mytable.find_one({'_id': ObjectId(attendee_id)}, {'STT': 1, 'Họ và tên': 1, 'Năm sinh': 1, 'Giới tính': 1, 'Trường': 1, 'Chuyên ngành': 1})
        if attendee_info:
            attendee_info['_id'] = str(attendee_info['_id'])
            return render_template('profile.html', attendee=attendee_info)
        else:
            return render_template('profile.html', error='Attendee not found')

    @app.route('/create')
    def create():
        return render_template('create.html')

    @app.route('/api/table')
    def table_data():
        data = list(db.mytable.find({}, {'_id': 1, 'Họ và tên': 1}))
        formatted_data = []
        for doc in data:
            formatted_doc = {}
            for field in doc:
                if field == '_id':
                    formatted_doc[field] = str(doc[field])
                else:
                    formatted_doc[field] = doc[field]
            formatted_data.append(formatted_doc)
        return jsonify(formatted_data)


    @app.route('/get/<string:id>')
    def get_info(id):
        try:
            attendee_id = ObjectId(id)
            attendee = db.mytable.find_one({'_id': attendee_id}, {'Họ và tên': 1, 'Năm sinh': 1, 'Giới tính': 1, 'Trường': 1, 'Chuyên ngành': 1})
            if attendee:
                attendee['_id'] = str(attendee['_id'])
                return jsonify({'attendee': attendee})
            else:
                return jsonify({'error': 'Attendee not found'})
        except ObjectId.InvalidId:
            return jsonify({'error': 'Invalid ID'})

        
    @app.route('/api/write_data', methods=['POST'])
    def write_data():
        data = request.form.to_dict()
        db.mytable.insert_one(data)
        return redirect('/')

    @app.route('/api/delete_entry', methods=['POST'])
    def delete_entry():
        entry_name = request.form.get('entry_name')
        result = db.mytable.delete_one({'Họ và tên': entry_name})

        if result.deleted_count == 1:
            return redirect('/')
        else:
            return jsonify({'message': 'Failed to delete entry'})


    @app.route('/api/update_entry', methods=['POST'])
    def update_entry():
        entry_id = request.form.get('_id')
        ho_ten = request.form.get('ho_ten')
        nam_sinh = request.form.get('nam_sinh')
        gioi_tinh = request.form.get('gioi_tinh')
        truong = request.form.get('truong')
        chuyen_nganh = request.form.get('chuyen_nganh')
        entry_id = ObjectId(entry_id)
        db.mytable.update_one(
            {'_id': entry_id},
            {'$set': {'Họ và tên': ho_ten, 'Năm sinh': nam_sinh, 'Giới tính': gioi_tinh, 'Trường': truong, 'Chuyên ngành': chuyen_nganh}}
        )
        return redirect('/')

    @app.route('/api/create-database', methods=['POST'])
    def create_database_api():
        if db.mytable.count_documents({}) == 0:
            with open('static/attendees.csv', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                rows = []
                counter = 0
                for row in reader:
                    rows.append(row)
                    counter += 1
                db.mytable.insert_many(rows)
            
            return redirect('/')
        else:
            return 'Database already exists'

    return app, db

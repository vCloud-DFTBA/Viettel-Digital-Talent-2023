from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_restful import Resource, Api
from pymongo import MongoClient

application = Flask(__name__)
api = Api(application)


def get_db():
    client = MongoClient(host='mongodb_host',
                         port=27017,
                         username='root',
                         password='123',
                         authSource="admin")
    db = client.students_db
    return client, db


client, db = get_db()


@application.route('/')
def index():
    students = db.students.find()
    return render_template('index.html', students=students)


@application.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        record = {
            'STT': request.form['stt'],
            'Họ và tên': request.form['hovaten'],
            'Username': request.form['username'],
            'Năm sinh': request.form['namsinh'],
            'Giới tính': request.form['gioitinh'],
            'Trường': request.form['truong'],
            'Chuyên ngành': request.form['chuyennganh']
        }
        db.students.insert_one(record)
        return redirect(url_for('index'))
    return render_template('create.html')


@application.route('/get/<id>', methods=['GET'])
def get(id):
    document = db.students.find_one({"STT": id})
    return render_template('get.html', document=document)

@application.route('/update/<string:id>', methods=['GET', 'POST'])
def update(id):
    document = db.students.find_one({'STT': id})
    if request.method == 'POST':
        record = {
            'STT': request.form['stt'],
            'Họ và tên': request.form['hovaten'],
            'Username': request.form['username'],
            'Năm sinh': request.form['namsinh'],
            'Giới tính': request.form['gioitinh'],
            'Trường': request.form['truong'],
            'Chuyên ngành': request.form['chuyennganh']
        }
        db.students.update_one({'STT': id}, {"$set": record})
        return redirect(url_for('index'))
    return render_template('update.html', document=document)


@application.route('/delete/<id>', methods=["GET", "DELETE"])
def delete(id):
    db.students.delete_one({'STT': id})
    return redirect(url_for('index'))




if __name__ == "__main__":
    unittest.main()

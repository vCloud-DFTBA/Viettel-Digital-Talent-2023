from flask import Flask, render_template
from pymongo import MongoClient

application = Flask(__name__)


def get_db():
    client = MongoClient(host='mongodb_host',
                         port=27017,
                         username='root',
                         password='123',
                         authSource="admin")
    db = client.students_db
    return db


@application.route('/')
def get_data():
    db = ""
    try:
        db = get_db()
        students = db.students.find()
        return render_template('index.html', students=students)
    except Exception as e:
        print(Exception)
    finally:
        if type(db) == MongoClient:
            db.close()


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000)

from app import create_app
from pymongo import MongoClient

client = MongoClient('mongodb://mongo_test_1:27017')
app, db = create_app(client, 'vdt_attendees_2023')

if __name__ == '__main__':
    app.run(debug=True, use_debugger=False, use_reloader=False, host="0.0.0.0")



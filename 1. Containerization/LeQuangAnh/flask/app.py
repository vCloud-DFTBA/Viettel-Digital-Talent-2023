from flask import Flask, render_template
from pymongo import MongoClient
from database_mod import create_database
import os
app = Flask(__name__)
client = MongoClient("mongodb://database:27017")
db = client["vdt2023_attendees"]
if db.mytable.count_documents({}) == 0:
    create_database(db)
@app.route('/')
def table():
    attendees = db.mytable.find()
    return render_template('table.html', attendees=attendees, header_color=os.environ['COLOR'])
if __name__ == '__main__':
    app.run(debug=True, use_debugger=False, use_reloader=False, host="0.0.0.0")

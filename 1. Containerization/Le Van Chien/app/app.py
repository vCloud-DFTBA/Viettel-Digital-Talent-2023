from flask import Flask
from flask import render_template
from pymongo import MongoClient
import pandas

app = Flask(__name__)
print('start')
@app.route('/')
def hello():
    client = MongoClient('mongodb://db:27017')
    db = client.attendee
    # counter =  db.counter.find_one({'_id': 1})
    # if counter is None:
    #     counter = {'_id': 1, 'count': 0}
    #     db.counter.insert_one(counter)
    # else:
    #     db.counter.update_one({'_id': 1}, {'$inc': {'count': 1}})
    #db = client.testDMBS
    #customer = db.Customer.find_one({'customerId':8})
    
    #return 'Hello, World! You have visited this page {} time'.format(counter['count'])

    if 'attendees' not in db.list_collection_names():
        df = pandas.read_csv("attendees.csv")
        listAttendees = [{'name': df.iloc[i, 1], 'school': df.iloc[i, 4]} for i in range(df.shape[0])]
        db.attendees.insert_many(listAttendees)
    
    attendees = list(db.attendees.find({}))
    # return render_template('index.html', count=counter['count'])
    return render_template('index.html', attendees=attendees)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

import os
import socket
from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson import ObjectId 

application = Flask(__name__, template_folder='template')

# hostname = socket.getfqdn()
# host_ip = socket.gethostbyname_ex(hostname)[2][0]

ret = os.system("ping -n -c 3 -W 3000 192.168.40.128")
if ret != 0:
	application.config["MONGO_URI"] = "mongodb://localhost:27017/VDT23"
else:
	application.config["MONGO_URI"] = "mongodb://192.168.40.128:27017/VDT23"
mongo = PyMongo(application)
db = mongo.db

@application.route("/")
def lists ():
	curs = db.attendees.find()
	a1="active"
	return render_template('index.html',a1=a1,curs=curs)

@application.route("/action", methods=['POST'])
def action ():
	Name=request.values.get("Name")
	DOB=request.values.get("DOB")
	Gender=request.values.get("Gender")
	University=request.values.get("University")
	Major=request.values.get("Major")
	Username=request.values.get("Username")
	db.attendees.insert_one({ "Name":Name, "DOB":DOB, "Gender":Gender, "University":University, "Major":Major, "Username": Username})
	return redirect("/")

@application.route("/remove")
def remove ():
	key=request.values.get("_id")
	db.attendees.delete_one({"_id":ObjectId(key)})
	return redirect("/")

@application.route("/update")
def update ():
	key=request.values.get("_id")
	curs=db.attendees.find({"_id":ObjectId(key)})
	return render_template('update.html',curs=curs)

@application.route("/action3", methods=['POST'])
def action3 ():
	Name=request.values.get("Name")
	DOB=request.values.get("DOB")
	Gender=request.values.get("Gender")
	University=request.values.get("University")
	Major=request.values.get("Major")
	Username=request.values.get("Username")
	key=request.values.get("_id")
	db.attendees.update_one({"_id":ObjectId(key)}, {'$set':{"Name":Name, "DOB":DOB, "Gender":Gender, "University":University, "Major":Major, "Username":Username}})
	return redirect("/")

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000, debug=True)

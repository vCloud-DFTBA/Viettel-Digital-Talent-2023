from flask import Flask, render_template, request, redirect
import csv
from pymongo import MongoClient


app = Flask(__name__)


client = MongoClient("mongodb://db:27017/")
db = client["internees"]



@app.route("/")
def index():
    return render_template("index.html", attendees=db.internees.find())

@app.route("/addStudent", methods = ['GET','POST'])
def addcar():
    if request.method == 'GET':
        return render_template("addStudent.html")
    if request.method == 'POST':
        id = int(request.form["STT"])
        name = request.form["name"]
        year = int(request.form["year"])
        gender = request.form["gender"]
        school = request.form["school"]
        major = request.form["major"]
        db.internees.insert_one({'STT':id, 'name':name, 'year' : year, 'gender' : gender, 'school' : school, 'major' : major})
        return redirect('/')


@app.route('/deleteStudent/<int:id>')
def deleteStudent(id):
    db.internees.delete_one({"STT":id})
    return redirect('/')


@app.route('/view/<int:id>')
def viewStudent(id):
    students = []
    students.append(db.internees.find_one({"STT": id}))
    return render_template("detail.html", students=students)
@app.route('/updateStudent/<int:id>',methods = ['GET','POST'])
def updatecar(id):
    students = []
    if request.method == 'GET':
        students.append(db.internees.find_one({"STT":id}))
        return render_template("updateStudent.html", students = students)
    if request.method == 'POST':
        name = request.form["name"]
        year = int(request.form["year"])
        gender = request.form["gender"]
        school = request.form["school"]
        major = request.form["major"]
        db.internees.update_one({'STT':id}, {"$set" : {'name':name, 'year' : year, 'gender' : gender, 'school' : school, 'major' : major}})
        return redirect('/')

if __name__=='__main__':
    app.run(host='0.0.0.0', port=9090, debug=True)

from data import students


import json


def addDB():
    for student in students:
        print(student)
        print(type(json.dumps(student)))


addDB()

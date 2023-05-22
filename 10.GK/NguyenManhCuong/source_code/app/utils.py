from bson import ObjectId
def insert_attendee(collection, attendee):
    if collection.find_one(sort=[("stt", -1)]):
        attendee['stt'] = int(collection.find_one(sort=[("stt", -1)])["stt"]) + 1
    else:
        attendee['stt'] = 1
    result = collection.insert_one(attendee)
    return result

def delete_attendee(collection, attendee_id):
    attendee = collection.find_one({"_id": ObjectId(attendee_id)})
    if attendee:
        stt = attendee["stt"]
        collection.delete_one({"_id": ObjectId(attendee_id)})
        collection.update_many({"stt": {"$gt": stt}}, {"$inc": {"stt": -1}})

def create_student_from_form(form):
    return {
        'name': form['name'],
        'username': form['username'],
        'birth_year': form['birth_year'],
        'gender': form['gender'],
        'university': form['university'],
        'major': form['major']
    }
    
def create_formatted_student(student):
    return {
        '_id': str(student['_id']),
        'stt': student['stt'],
        'name': student['name'],
        'username': student['username'],
        'birth_year': student['birth_year'],
        'gender': student['gender'],
        'university': student['university'],
        'major': student['major']
    }
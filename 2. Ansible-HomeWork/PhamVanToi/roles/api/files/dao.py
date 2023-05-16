from pymongo import MongoClient

def get_db():

    client = MongoClient("mongodb://mongodb-server:27017/")
    db = client["internees"]
    return db

def insert_data(id = '', name= '', username= '', birth = '', sex = '', university = '', major = ''):
    try:
        db = get_db()
        db.internees.insert_one({'id':id, 'name': name, 'username': username , 'birth': birth, 'sex': sex , 'university': university, 'major': major})
    except:
        pass
    finally:
        if type(db)==MongoClient:
            db.close()

def delete_data(id = ''):
    try:
        db = get_db()
        db.internees.delete_one({'id':id})
    except:
        pass
    finally:
        if type(db)==MongoClient:
            db.close()

def update_data(id = '', name= '', username= '', birth = '', sex = '', university = '', major = ''):
    try:
        db = get_db()
        db.internees.update_one({'id': id}, {'$set': {'name': name, 'username': username , 'birth': birth, 'sex': sex , 'university': university, 'major': major}})
    except:
        pass
    finally:
        if type(db)==MongoClient:
            db.close()

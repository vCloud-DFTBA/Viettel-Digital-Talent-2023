# model student connect to database mongodb
from app.models import collection as db
from unidecode import unidecode

class Intern:
    def __init__(self, name, university, year_of_birth):
        self.name = name
        self.university = university
        self.year_of_birth = year_of_birth
        unicode_name = unidecode(self.name) 
        self.email = unicode_name.split(' ')[-1].lower() + unicode_name.split(' ')[0][0].lower() + unicode_name.split(' ')[1][0].lower() + '@' + 'is.viettel.com.vn'
    
    def save(self):
        # Check if intern already exists
        if db.find_one({'name': self.name, 'university': self.university, 'year_of_birth': self.year_of_birth}):
            return False
        db.insert_one({
            'name': self.name,
            'university': self.university,
            'year_of_birth': self.year_of_birth,
            'email': self.email
        })
    
    @classmethod
    def get_all(cls):
        interns = []
        for intern in db.find():
            interns.append({
                'id': str(intern['_id']),
                'name': intern['name'],
                'university': intern['university'],
                'email': intern['email'],
                'year_of_birth': intern['year_of_birth']
            })
        return interns

    @classmethod
    def get_by_id(cls, id):
        return db.find_one({'_id': id})
    
    def update(self, id):
        unicode_name = unidecode(self.name)
        email = unicode_name.split(' ')[-1].lower() + unicode_name.split(' ')[0][0].lower() + unicode_name.split(' ')[1][0].lower() + '@' + 'is.viettel.com.vn'
        db.update_one({'_id': id}, {'$set': {
            'name': self.name,
            'university': self.university,
            'year_of_birth': self.year_of_birth,
            'email': email
        }})
    
    @classmethod
    def delete(cls, id):
        db.delete_one({'_id': id})

    # Delete many
    @classmethod
    def delete_many(cls, ids):
        db.delete_many({'_id': {'$in': ids}})

    # Delete all
    @classmethod
    def delete_all(cls):
        db.delete_many({})
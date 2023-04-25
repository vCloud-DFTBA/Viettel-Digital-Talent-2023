from flask import request, jsonify
from app.controllers import intern_blueprint
from app.models.intern import Intern

@intern_blueprint.route('/', methods=['GET'])
def get_all_interns():
    return jsonify(Intern.get_all())


@intern_blueprint.route('/', methods=['POST'])
def create_intern():
    print(request.json)
    intern = Intern(request.json['name'], request.json['university'], request.json['year_of_birth'])
    return jsonify(intern.save())

# Update intern by id
@intern_blueprint.route('/<id>', methods=['PUT'])
def update_intern(id):
    print(id)
    intern = Intern(request.json['name'], request.json['university'], request.json['year_of_birth'])
    return jsonify(intern.update(id))
from flask import request, jsonify
from app.controllers import intern_blueprint
from app.models.intern import Intern

@intern_blueprint.route('/', methods=['GET'])
def get_all_interns():
    return jsonify(Intern.get_all())


@intern_blueprint.route('/', methods=['POST'])
def create_intern():
    return jsonify(Intern.create(request.json))
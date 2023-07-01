from flask import Blueprint

intern_blueprint = Blueprint('interns', __name__)

from app.controllers import intern

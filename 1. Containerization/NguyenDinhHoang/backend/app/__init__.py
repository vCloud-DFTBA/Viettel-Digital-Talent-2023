from flask import Flask
from flask_cors import CORS
from app.init_database import init_db

from config import Config

init_db()

def create_app(config_class=Config):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config_class)
    # debug mode
    
    from app.controllers import intern_blueprint
    app.register_blueprint(intern_blueprint, url_prefix='/interns')

    @app.route('/test')
    def test_page():
        return 'Testing the Flask Application Factory Pattern'
    return app
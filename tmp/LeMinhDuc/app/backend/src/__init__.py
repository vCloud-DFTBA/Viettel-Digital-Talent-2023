from flask import Flask
from flask_cors import CORS


def create_app(custom_config=None):
    app = Flask(__name__)
    CORS(app)

    app.config.from_pyfile("config.py", silent=True)
    if custom_config:
        app.config.update(custom_config)

    from src.db import get_db, init_app

    init_app(app)
    db = get_db()
    if not "cloud" in db.list_collection_names():
        cloud_collection = db["cloud"]

    from src.controllers import CloudController

    app.add_url_rule(
        "/cloud",
        methods=["GET"],
        view_func=CloudController.get_all,
    )
    app.add_url_rule(
        "/cloud",
        methods=["POST"],
        view_func=CloudController.create,
    )
    app.add_url_rule(
        "/cloud/<int:id>",
        methods=["GET"],
        view_func=CloudController.get_one,
    )
    app.add_url_rule(
        "/cloud/<int:id>",
        methods=["PATCH"],
        view_func=CloudController.update,
    )
    app.add_url_rule(
        "/cloud/<int:id>",
        methods=["DELETE"],
        view_func=CloudController.remove,
    )

    return app

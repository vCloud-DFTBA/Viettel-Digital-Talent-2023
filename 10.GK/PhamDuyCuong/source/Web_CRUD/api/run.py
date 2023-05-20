import os
from Flask_CRUD.app import create_app
from Flask_CRUD.db import init_db

db = init_db()
app = create_app(db)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get("FLASK_SERVER_PORT"), debug=True)

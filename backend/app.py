from flask import Flask

from backend.apis import api
from backend.postgres import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:password@localhost:5432/demo"

api.init_app(app)
db.init_app(app)


if __name__ == "__main__":
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)

from flask import Flask
from flask_marshmallow import Marshmallow

from backend.apis import api
from backend.postgres import db

ma = Marshmallow()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://admin:password@localhost:5432/demo"

api.init_app(app)
db.init_app(app)
ma.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)

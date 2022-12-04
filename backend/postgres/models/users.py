# from flask_marshmallow.sqla import SQLAlchemyAutoSchema
# from sqlalchemy import Column, ForeignKey, Integer, String

from backend.postgres import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    description = db.Column(db.String)

    def __init__(self, name, last_name, email, description):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.description = description

    def __repr__(self):
        return f"User(name={self.name})"


# class UserSchema(SQLAlchemyAutoSchema):
#     class Meta:
#         model = User
#         load_instance = True
#         include_fk = True
#         sqla_session = db.session


# user_schema = UserSchema()

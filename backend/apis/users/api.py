from flask_restx import Namespace, Resource

from backend.postgres.models.users import User

api = Namespace("users")


@api.route("/")
class AllUsers(Resource):
    def get(self):
        from backend.postgres import db

        users = db.session.query(User).all()
        return "It worked :)"


@api.route("/<string:user_name>")
class AllUsers(Resource):
    def get(self, user_name):
        from backend.postgres import db

        user = User(
            name=user_name,
            last_name="ramirez",
            email="adrian.ramirez@mail.com",
            description="This is a description",
        )
        db.session.add(user)
        db.session.commit()

        return

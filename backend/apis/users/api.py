from flask_restx import Namespace, Resource

api = Namespace("users")


@api.route("/")
class AllUsers(Resource):
    def get(self):
        pass

from flask_restx import Namespace, Resource, reqparse

from backend.apis.todos.models import todo_model, todos_model
from backend.core.database import Todo, Todos
from backend.core.utils import get_key

api = Namespace("todos", description="All related to Todos")


parser = reqparse.RequestParser()
parser.add_argument(
    "description",
    type=str,
    help="Todo Description",
)


todos = Todos()


@api.route("/<string:todo_id>")
class TodoSimple(Resource):
    @api.marshal_with(todo_model(api))
    def get(self, todo_id):
        todo = todos.get_by_id(todo_id)
        return todo

    @api.marshal_with(todo_model(api))
    def put(self, todo_id):
        description = get_key(parser, "description")
        todos.add(Todo(todo_id, description))
        return todos.get_by_id(todo_id)


@api.route("/")
class AllTodos(Resource):
    @api.marshal_with(todos_model(api))
    def get(self):
        return todos

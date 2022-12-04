from dataclasses import dataclass
from typing import List, Optional

from flask import Flask
from flask_restx import Api, Resource, reqparse

from models import todo_model, todos_model

app = Flask(__name__)
api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument("description", type=str, help="Todo Description")


def get_key(_parser: reqparse.RequestParser, key: str):
    args = _parser.parse_args(strict=True)
    return args.get(key)


@dataclass
class Todo:
    todo_id: int
    description: str


@dataclass
class Todos:
    elements: List[Todo] = None

    def __post_init__(self):
        if self.elements is None:
            self.elements = []

    def get_by_id(self, _todo_id: int) -> Optional[Todo]:
        for todo in self.elements:
            if todo.todo_id == _todo_id:
                return todo
        return self.create_empty_todo()

    def add(self, todo: Todo):
        self.elements.append(todo)

    def __str__(self):
        all_todos = ",\n".join([str(element) for element in self.elements])
        return f"Todos: {all_todos}"

    @classmethod
    def create_empty_todo(cls):
        return Todo(None, None)


todos = Todos()


@api.route("/todos/<string:todo_id>")
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


@api.route("/todos/all")
class AllTodos(Resource):
    @api.marshal_with(todos_model(api))
    def get(self):
        return todos


if __name__ == "__main__":
    app.run(debug=True)

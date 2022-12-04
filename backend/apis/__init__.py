from flask_restx import Api

from backend.apis.todos.api import api as todos
from backend.apis.users.api import api as users

api = Api()

api.add_namespace(todos)
api.add_namespace(users)

from flask_restx import Namespace, fields


def todo_model(_api: Namespace):
    return _api.model(
        "Todo Model",
        {
            "todo_id": fields.Integer,
            "description": fields.String,
        },
    )


def todos_model(_api: Namespace):
    return _api.model(
        "Todos Model",
        {
            "elements": fields.List(fields.Nested(todo_model(_api))),
        },
    )

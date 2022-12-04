from flask_restx import reqparse


def get_key(parser: reqparse.RequestParser, key: str):
    args = parser.parse_args(strict=True)
    return args.get(key)

from flask import jsonify
from app import app


class OneOmeError(Exception):
    pass


class BadRequestException(OneOmeError):
    code = 400
    description = 'Bad Request'


@app.errorhandler(OneOmeError)
def handle_exception(err):
    response = {'error': err.description, 'message': ''}
    if len(err.args) > 0:
        response['message'] = err.args[0]
    return jsonify(response), err.code


@app.errorhandler(500)
def handle_500exception(err):
    response = {'error': 'Unknown error', 'message': 'Unknown error. Please contact administrator.'}
    return jsonify(response), 500

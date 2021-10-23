import sqlalchemy
from flask import Blueprint, jsonify
from flask_json_schema import JsonValidationError

mod_errors = Blueprint('errors', __name__)


@mod_errors.app_errorhandler(JsonValidationError)
def validation_error(e):
    return jsonify(
        {'error': e.message, 'errors': [validation_error.message for validation_error in e.errors]}), 400


@mod_errors.app_errorhandler(sqlalchemy.exc.IntegrityError)
def validation_error(e):
    return jsonify(e.args), 400

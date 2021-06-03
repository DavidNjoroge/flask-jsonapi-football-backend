from flask import Blueprint

mod_errors = Blueprint('errors', __name__)

# not working
@mod_errors.errorhandler(Exception)
def uncaught_errors(error):
    return {"message": 500}, 500


@mod_errors.errorhandler(404)
def not_found(error):
    return {"message": 404}, 404

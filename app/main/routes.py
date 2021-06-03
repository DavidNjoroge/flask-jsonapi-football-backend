# Import flask dependencies
from flask import Blueprint

# Import the database object from the main app module
# from app import db

# Import module models (i.e. User)
from app.main.models import User

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_main = Blueprint('main', __name__, url_prefix='/main')


# Set the route and accepted methods
@mod_main.route('/', methods=['GET', 'POST'])
def main_example():

    return {
        'content': [],
        'page': 1,
        'results_per_page': 5,
        'total_results': 100
    }

# Import module models (i.e. User)
from app.main import mod_main
from app.main.models import User

# Define the blueprint: 'auth', set its url prefix: app.url/auth
from app.main.schemas import UserSchema


# Set the route and accepted methods
@mod_main.route('/', methods=['GET', 'POST'])
def main_example():
    return {
        'content': [],
        'page': 1,
        'results_per_page': 5,
        'total_results': 100
    }


@mod_main.route('/users', methods=['GET', 'POST'])
def fetch_users():
    return UserSchema(many=True).dumps(User.query.all())

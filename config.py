
class DefaultConfig:
    # Default for localhost
    # Statement for enabling the development environment
    DEBUG = True

    # Define the application directory
    import os

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Define the database - we are working with
    # SQLite for this example
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres_user:password@localhost:5438/postgres'
    DATABASE_CONNECT_OPTIONS = {}

    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED = True

    # Use a secure, unique and absolutely secret key for
    # signing the data.
    CSRF_SESSION_KEY = "secret"

    # Secret key for signing cookies
    SECRET_KEY = "secret"

    SQLALCHEMY_TRACK_MODIFICATIONS=True


class HerokuConfig:
    # Statement for enabling the development environment
    DEBUG = True

    # Define the application directory
    import os

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Define the database - we are working with
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    DATABASE_CONNECT_OPTIONS = {}

    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED = True

    # Use a secure, unique and absolutely secret key for
    # signing the data.
    CSRF_SESSION_KEY = "secret"

    # Secret key for signing cookies
    SECRET_KEY = "secret"

    SQLALCHEMY_TRACK_MODIFICATIONS=True

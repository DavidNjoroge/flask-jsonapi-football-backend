
class DefaultConfig:
    # Default for localhost
    DEBUG = True

    import os

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # testing local db
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres_user:password@localhost:5438/postgres'
    DATABASE_CONNECT_OPTIONS = {}

    CSRF_ENABLED = True

    # Use a secure, unique and absolutely secret key for
    # signing the data.
    CSRF_SESSION_KEY = "secret"

    # Secret key for signing cookies
    SECRET_KEY = "secret"

    SQLALCHEMY_TRACK_MODIFICATIONS=True


class HerokuConfig:
    DEBUG = True

    import os

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    DATABASE_CONNECT_OPTIONS = {}

    CSRF_ENABLED = True

    CSRF_SESSION_KEY = os.environ.get('SECRET_KEY')

    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_TRACK_MODIFICATIONS=True

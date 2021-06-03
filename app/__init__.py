# Import flask and template operators
from flask import Flask

# Define the WSGI application object
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restless import APIManager
from flask_sqlalchemy import SQLAlchemy

# Define the database object which is imported
# by modules and controllers
from config import DefaultConfig

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
manager = APIManager()


# # Sample HTTP error handling
# @app.errorhandler(404)
# def not_found(error):
#     return render_template('404.html'), 404

def create_app():
    app = Flask(__name__)
    app.config.from_object(DefaultConfig)

    db.init_app(app)
    migrate.init_app(app=app, db=db)
    ma.init_app(app)
    manager.init_app(app, flask_sqlalchemy_db=db)

    with app.app_context():
        from app.main.routes import mod_main as main_module

        app.register_blueprint(main_module)
        from app.custom_errors import mod_errors
        app.register_blueprint(mod_errors)
        from app.mod_restless import restless_bp
        app.register_blueprint(restless_bp)

        from app.main.models import User

        return app

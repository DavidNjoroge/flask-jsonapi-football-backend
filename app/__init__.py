# Import flask and template operators
from flask import Flask, render_template


# Define the WSGI application object
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy




# Define the database object which is imported
# by modules and controllers
from config import DefaultConfig

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()

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
    # Configurations
    from app.main.routes import mod_main as main_module

    app.register_blueprint(main_module)
    return app



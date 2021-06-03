from flask import Blueprint, current_app
from flask_restless import APIManager

from app import db, manager
from app.main.models import User

restless_bp = Blueprint('api', __name__)


manager.create_api(User, collection_name='users', methods=['GET', 'POST', 'PUT', 'DELETE'], app=current_app)

from flask import Blueprint, current_app

from app import manager
from app.main.models import League, Fixture, TeamPlayer, LeagueTeam, Team, Season, Player

restless_bp = Blueprint('api', __name__)


manager.create_api(League, collection_name='leagues', methods=['GET', 'POST', 'PUT', 'DELETE'], app=current_app)
manager.create_api(Fixture, collection_name='fixtures', methods=['GET', 'POST', 'PUT', 'DELETE'], app=current_app)
manager.create_api(TeamPlayer, collection_name='teamPlayers', methods=['GET', 'POST', 'PUT', 'DELETE'], app=current_app)
manager.create_api(LeagueTeam, collection_name='leagueTeams', methods=['GET', 'POST', 'PUT', 'DELETE'], app=current_app)
manager.create_api(Team, collection_name='teams', methods=['GET', 'POST', 'PUT', 'DELETE'], app=current_app)
manager.create_api(Season, collection_name='seasons', methods=['GET', 'POST', 'PUT', 'DELETE'], app=current_app)
manager.create_api(Player, collection_name='players', methods=['GET', 'POST', 'PUT', 'DELETE'], app=current_app)

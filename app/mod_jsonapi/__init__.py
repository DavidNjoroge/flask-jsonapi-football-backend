from flask import Blueprint

from app import jsonApi

rest_api_bp = Blueprint('rest_api', __name__, url_prefix='/jsonapi')

from app.mod_jsonapi.resources import LeagueList, LeagueDetail, FixtureList, FixtureDetail

# note: first param must not be shared among routes
jsonApi.route(LeagueList, 'league_list', 'leagues', blueprint=rest_api_bp)
jsonApi.route(LeagueDetail, 'league_detail', '/leagues/<int:id>', blueprint=rest_api_bp)


jsonApi.route(FixtureList, 'fixture_list', 'fixtures', blueprint=rest_api_bp)
jsonApi.route(FixtureDetail, 'fixture_detail', '/fixtures/<int:id>', blueprint=rest_api_bp)


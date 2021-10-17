from flask import Blueprint

from app import jsonApi

rest_api_bp = Blueprint('rest_api', __name__, url_prefix='/jsonapi')

from app.mod_jsonapi.resources import LeagueList, LeagueDetail, FixtureList, FixtureDetail, SeasonDetail, SeasonList, \
    TeamDetail, TeamList

# note: first param must not be shared among routes
jsonApi.route(LeagueList, 'league_list', 'leagues', blueprint=rest_api_bp)
jsonApi.route(LeagueDetail, 'league_detail', '/leagues/<int:id>', blueprint=rest_api_bp)


jsonApi.route(FixtureList, 'fixture_list', 'fixtures', blueprint=rest_api_bp)
jsonApi.route(FixtureDetail, 'fixture_detail', '/fixtures/<int:id>', blueprint=rest_api_bp)


jsonApi.route(SeasonList, 'season_list', 'seasons', blueprint=rest_api_bp)
jsonApi.route(SeasonDetail, 'season_detail', '/seasons/<int:id>', blueprint=rest_api_bp)


jsonApi.route(TeamList, 'team_list', 'teams', blueprint=rest_api_bp)
jsonApi.route(TeamDetail, 'team_detail', '/teams/<int:id>', blueprint=rest_api_bp)


from app import schema, db
from app.main import mod_main
from app.main.helpers import create_save_fixture_response_dict
from app.main.mod_service.fixture_mod_service import FixtureModService
from app.main.mod_service.league_team_mod_service import LeagueTeamModService
from app.main.mod_service.team_mod_service import TeamModService
from flask import request, jsonify


teamModService = TeamModService.get_instance()
leagueTeamModService = LeagueTeamModService.get_instance()
fixtureModService = FixtureModService.get_instance()


# Set the route and accepted methods
@mod_main.route('/', methods=['GET', 'POST'])
def main_example():
    return {
        'content': [],
        'page': 1,
        'results_per_page': 5,
        'total_results': 100
    }


create_fixtures_schema = {
    'required': ['homeTeamName', 'awayTeamName', 'fixtureDate'],
    'properties': {
        'homeTeamName': { 'type': 'string' },
        'awayTeamName': { 'type': 'string' },
        'fixtureDate': { 'type': 'string' },
        'FTHG': { 'type': 'integer' },
        'FTAG': { 'type': 'integer' },
    }
}


@mod_main.route('season/<int:season_id>/league/<int:league_id>/create_fixtures', methods=['POST'])
@schema.validate(create_fixtures_schema, methods=['POST'])
def create_fixture(season_id, league_id):
    # request.get_json()
    # 1first check if team exists else create one
    # 2check if league team exists
    # 3check if fixture exists for fixtureDate
    # 4finally create fixture

    import json
    request_payload = json.loads(request.data)
    from dateutil.parser import parse
    parsed_fixture_date = parse(request_payload.get('fixtureDate'))

    season = leagueTeamModService.find_season(season_id=season_id)
    league = leagueTeamModService.find_league(league_id=league_id)

    # 1first check if team exists else create one
    home_team_results = teamModService.search_teams(request_payload.get('homeTeamName'))
    away_team_results = teamModService.search_teams(request_payload.get('awayTeamName'))

    if len(home_team_results) == 0:
        home_team = teamModService.create_team(request_payload.get('homeTeamName'))
        db.session.commit()
    else:
        home_team = home_team_results[0]

    if len(away_team_results) == 0:
        away_team = teamModService.create_team(request_payload.get('awayTeamName'))
        db.session.commit()
    else:
        away_team = away_team_results[0]

    # 2check if league team exists
    # home_league_team_results = teamModService.search_teams(request_payload.get('homeTeamName'))

    home_league_team = leagueTeamModService.find_league_team(season_id=season_id, league_id=league_id, team_id=home_team.id)
    away_league_team = leagueTeamModService.find_league_team(season_id=season_id, league_id=league_id, team_id=away_team.id)

    if home_league_team is None:
        home_league_team = leagueTeamModService.create_league_team(season=season, league=league, team=home_team)
        db.session.commit()

    if away_league_team is None:
        away_league_team = leagueTeamModService.create_league_team(season=season, league=league, team=away_team)
        db.session.commit()

    # fixtureDateFormat
    existing_fixture = fixtureModService.find_fixture(home_league_team=home_league_team, away_league_team=away_league_team, fixture_date=parsed_fixture_date)

    # todo create table constraint
    # if existing_fixture is not None:
    #     return jsonify({"message": "fixture already exists"}), 400
    # 4finally create fixture
    new_fixture = fixtureModService.create_fixture(
        home_league_team=home_league_team,
        away_league_team=away_league_team,
        fixture_date=parsed_fixture_date,
        home_score=request_payload.get('FTHG'),
        away_score=request_payload.get('FTAG')
    )

    db.session.commit()

    return jsonify(create_save_fixture_response_dict()), 201

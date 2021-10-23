from app import db
from app.main.models import LeagueTeam, Season, League


class LeagueTeamModService:
    __model__ = LeagueTeam
    __instance = None

    @staticmethod
    def get_instance():
        if not LeagueTeamModService.__instance:
            LeagueTeamModService.__instance = LeagueTeamModService()
        return LeagueTeamModService.__instance

    def search_teams(self, team_name):
        return self.__model__.query.filter(self.__model__.name.ilike(team_name)).all()

    def find_season(self, season_id):
        return Season.query.filter(Season.id==season_id).one()

    def find_league(self, league_id):
        return League.query.filter(League.id==league_id).one()

    def find_league_team(self, season_id, league_id, team_id):
        return self.__model__.query.filter(
            self.__model__.season_id==season_id,
            self.__model__.league_id==league_id,
            self.__model__.team_id==team_id).first()

    def create_league_team(self, season, league, team):
        new_league_team = self.__model__(season_id=season.id, league_id=league.id, team_id=team.id)
        db.session.add(new_league_team)
        return new_league_team

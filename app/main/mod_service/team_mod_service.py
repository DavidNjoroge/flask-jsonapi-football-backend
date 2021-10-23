from app import db
from app.main.models import Team


class TeamModService:
    __model__ = Team
    __instance = None

    @staticmethod
    def get_instance():
        if not TeamModService.__instance:
            TeamModService.__instance = TeamModService()
        return TeamModService.__instance

    def search_teams(self, team_name):
        return self.__model__.query.filter(self.__model__.name.ilike(team_name)).all()

    def create_team(self, name):
        new_team = self.__model__(name=name)
        db.session.add(new_team)
        return new_team

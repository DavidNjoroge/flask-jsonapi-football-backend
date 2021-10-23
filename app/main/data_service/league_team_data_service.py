from app.main.models import LeagueTeam


class LeagueTeamDataService:
    __model__ = LeagueTeam
    __instance = None

    @staticmethod
    def get_instance():
        if not LeagueTeamDataService.__instance:
            LeagueTeamDataService.__instance = LeagueTeamDataService()
        return LeagueTeamDataService.__instance

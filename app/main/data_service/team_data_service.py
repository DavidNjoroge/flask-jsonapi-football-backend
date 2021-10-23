from app.main.models import Team


class TeamDataService:
    __model__ = Team
    __instance = None

    @staticmethod
    def get_instance():
        if not TeamDataService.__instance:
            TeamDataService.__instance = TeamDataService()
        return TeamDataService.__instance

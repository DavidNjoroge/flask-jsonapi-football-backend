from app.main.models import Fixture


class FixtureDataService:
    __model__ = Fixture
    __instance = None

    @staticmethod
    def get_instance():
        if not FixtureDataService.__instance:
            FixtureDataService.__instance = FixtureDataService()
        return FixtureDataService.__instance

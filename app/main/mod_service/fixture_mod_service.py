from app import db
from app.main.models import Fixture


class FixtureModService:
    __model__ = Fixture
    __instance = None

    @staticmethod
    def get_instance():
        if not FixtureModService.__instance:
            FixtureModService.__instance = FixtureModService()
        return FixtureModService.__instance

    def find_fixture(self, home_league_team, away_league_team, fixture_date):
        return self.__model__.query.filter(
            self.__model__.home_id==home_league_team.id,
            self.__model__.away_id==away_league_team.id,
            self.__model__.fixture_date==fixture_date).first()

    def create_fixture(self, home_league_team, away_league_team, home_score, away_score, fixture_date):
        new_league_team = self.__model__(home_id=home_league_team.id, away_id=away_league_team.id, home_score=home_score, away_score=away_score, fixture_date=fixture_date)
        db.session.add(new_league_team)
        return new_league_team


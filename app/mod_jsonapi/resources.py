from flask_rest_jsonapi import ResourceList

from app import db
from app.main.models import League, Fixture, Season, Team
from app.mod_jsonapi.schemas import LeagueSchema, FixtureSchema, SeasonSchema, TeamSchema


class LeagueList(ResourceList):
    # def query(self, view_kwargs):
    #     query_ = self.session.query(League)
    #
    #     return query_

    methods = ['GET', 'POST']
    schema = LeagueSchema
    data_layer = {'session': db.session,
                  'model': League,
                  # 'methods': {'query': query}
                  }


# todo not finished
class LeagueDetail(ResourceList):
    schema = LeagueSchema
    data_layer = {'session': db.session,
                  'model': League,
                  }


class FixtureList(ResourceList):
    methods = ['GET']
    schema = FixtureSchema
    data_layer = {'session': db.session,
                  'model': Fixture,
                  # 'methods': {'query': query}
                  }


# todo not finished
class FixtureDetail(ResourceList):
    schema = FixtureSchema
    data_layer = {'session': db.session,
                  'model': Fixture,
                  }


class SeasonList(ResourceList):
    methods = ['GET', 'POST']
    schema = SeasonSchema
    data_layer = {'session': db.session,
                  'model': Season,
                  # 'methods': {'query': query}
                  }


class SeasonDetail(ResourceList):
    schema = SeasonSchema
    data_layer = {'session': db.session,
                  'model': Season,
                  }


class TeamList(ResourceList):
    methods = ['GET', 'POST']
    schema = TeamSchema
    data_layer = {'session': db.session,
                  'model': Team,
                  # 'methods': {'query': query}
                  }


class TeamDetail(ResourceList):
    schema = TeamSchema
    data_layer = {'session': db.session,
                  'model': Team,
                  }

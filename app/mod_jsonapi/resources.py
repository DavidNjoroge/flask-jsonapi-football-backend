from flask_rest_jsonapi import ResourceList, ResourceRelationship

from app import db
from app.main.models import League, Fixture, Season, Team, LeagueTeam
from app.mod_jsonapi.schemas import LeagueSchema, FixtureSchema, SeasonSchema, TeamSchema, LeagueTeamSchema


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
    methods = ['GET', 'POST']
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


class LeagueTeamList(ResourceList):
    methods = ['GET', 'POST']
    schema = LeagueTeamSchema
    data_layer = {'session': db.session,
                  'model': LeagueTeam,
                  # 'methods': {'query': query}
                  }


class LeagueTeamDetail(ResourceList):
    schema = LeagueTeamSchema
    data_layer = {'session': db.session,
                  'model': LeagueTeam,
                  }


class FixtureRelationship(ResourceRelationship):
    schema = FixtureSchema
    data_layer = {'session': db.session,
                  'model': Fixture}


class LeagueTeamRelationship(ResourceRelationship):
    schema = LeagueTeamSchema
    data_layer = {'session': db.session,
                  'model': LeagueTeam}


class LeagueTeamToLeagueRelationship(ResourceRelationship):
    schema = LeagueTeamSchema
    data_layer = {'session': db.session,
                  'model': LeagueTeam}

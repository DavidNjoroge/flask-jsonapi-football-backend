from marshmallow_jsonapi.fields import Relationship
from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields


class LeagueSchema(Schema):
    class Meta:
        type_ = 'league'
        self_view = 'rest_api.league_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'rest_api.league_list'

    id = fields.Integer(as_string=True, dump_only=True)
    name = fields.Str()
    description = fields.Str()
    max_teams = fields.Integer()
    # contracts = Relationship(self_view='rest_api.tenant_contracts',
    #                          self_view_kwargs={'id': '<id>'},
    #                          related_view='rest_api.contract_list',
    #                          related_view_kwargs={'tenant_id': '<id>'},
    #                          many=True,
    #                          schema='JsonApiContractSchema',
    #                          type_='contract')


class FixtureSchema(Schema):
    class Meta:
        type_ = 'fixture'
        self_view = 'rest_api.fixture_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'rest_api.fixture_list'

    id = fields.Integer(as_string=True, dump_only=True)
    away_score = fields.Str()
    fixture_date = fields.Str()
    fixture_time = fields.Str()
    home_score = fields.Str()
    match_week = fields.Str()
    results = fields.Str()
    away_id = fields.Str()
    home_id = fields.Str()
    home = Relationship(attribute='home',
                         self_view='fixture_team',
                         self_view_kwargs={'id': '<id>'},
                         related_view='league_team_detail',
                         # related_view_kwargs={'home_id': '<id>'},
                         schema='LeagueTeamSchema',
                         type_='league_team')

    away = Relationship(attribute='away',
                         self_view='fixture_team',
                         self_view_kwargs={'id': '<id>'},
                         related_view='league_team_detail',
                         schema='LeagueTeamSchema',
                         type_='league_team')




class SeasonSchema(Schema):
    class Meta:
        type_ = 'season'
        self_view = 'rest_api.season_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'rest_api.season_list'

    id = fields.Integer(as_string=True, dump_only=True)
    end_year = fields.Str()
    start_year = fields.Str()
    # description = fields.Str()
    # max_teams = fields.Integer()


class TeamSchema(Schema):
    class Meta:
        type_ = 'team'
        self_view = 'rest_api.team_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'rest_api.team_list'

    id = fields.Integer(as_string=True, dump_only=True)
    date_founded = fields.Str()
    location = fields.Str()
    name = fields.Str()
    manager = fields.Str()


class LeagueTeamSchema(Schema):
    class Meta:
        type_ = 'league_team'
        self_view = 'rest_api.league_team_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'rest_api.league_team_list'

    id = fields.Integer(as_string=True, dump_only=True)
    date_joined = fields.Str()
    league_id = fields.Integer()
    season_id = fields.Integer()
    team_id = fields.Integer()

    team = Relationship(attribute='team',
                         self_view='league_team_to_team',
                         self_view_kwargs={'id': '<id>'},
                         related_view='team_detail',
                         schema='TeamSchema',
                         type_='team')



    league = Relationship(attribute='league',
                         self_view='league_team_to_league',
                         self_view_kwargs={'id': '<id>'},
                         related_view='league_detail',
                         schema='LeagueSchema',
                         type_='league')



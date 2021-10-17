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

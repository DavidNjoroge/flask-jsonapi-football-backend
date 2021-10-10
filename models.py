# coding: utf-8
from sqlalchemy import BigInteger, Column, Date, ForeignKey, Integer, String, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class League(Base):
    __tablename__ = 'league'

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('league_id_seq'::regclass)"))
    description = Column(String(255))
    max_teams = Column(BigInteger)
    name = Column(String(255), nullable=False)


class Player(Base):
    __tablename__ = 'player'

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('player_id_seq'::regclass)"))
    date_of_birth = Column(Date)
    name = Column(String(255), nullable=False)
    preferred_position = Column(String(255))
    shirt_number = Column(BigInteger)


class Season(Base):
    __tablename__ = 'season'

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('season_id_seq'::regclass)"))
    end_year = Column(Date, nullable=False)
    start_year = Column(Date, nullable=False)


class Team(Base):
    __tablename__ = 'team'

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('team_id_seq'::regclass)"))
    date_founded = Column(Date)
    location = Column(String(255))
    manager = Column(String(255))
    name = Column(String(255), nullable=False)


class LeagueTeam(Base):
    __tablename__ = 'league_team'

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('league_team_id_seq'::regclass)"))
    date_joined = Column(Date)
    league_id = Column(ForeignKey('league.id'), nullable=False, server_default=text("nextval('league_team_league_id_seq'::regclass)"))
    season_id = Column(ForeignKey('season.id'), nullable=False, server_default=text("nextval('league_team_season_id_seq'::regclass)"))
    team_id = Column(ForeignKey('team.id'), nullable=False)

    league = relationship('League')
    season = relationship('Season')
    team = relationship('Team')


class TeamPlayer(Base):
    __tablename__ = 'team_player'

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('team_player_id_seq'::regclass)"))
    date_joined = Column(Date)
    player_id = Column(ForeignKey('player.id'), nullable=False)
    team_id = Column(ForeignKey('team.id'), nullable=False)

    player = relationship('Player')
    team = relationship('Team')


class Fixture(Base):
    __tablename__ = 'fixture'

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('fixture_id_seq'::regclass)"))
    away_score = Column(BigInteger)
    fixture_date = Column(Date, nullable=False)
    fixture_time = Column(String(255))
    home_score = Column(BigInteger)
    match_week = Column(BigInteger, nullable=False)
    results = Column(String(255))
    away_id = Column(ForeignKey('league_team.id'), nullable=False)
    home_id = Column(ForeignKey('league_team.id'), nullable=False)

    away = relationship('LeagueTeam', primaryjoin='Fixture.away_id == LeagueTeam.id')
    home = relationship('LeagueTeam', primaryjoin='Fixture.home_id == LeagueTeam.id')

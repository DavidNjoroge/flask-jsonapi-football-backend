from sqlalchemy import Column, BigInteger, String, Date, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from app import db


# Define a base model for other database tables to inherit
class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

class League(Base):
    __tablename__ = 'league'

    id = Column(BigInteger, primary_key=True)
    description = Column(String(255))
    max_teams = Column(BigInteger)
    name = Column(String(255), nullable=False)


class Player(Base):
    __tablename__ = 'player'

    id = Column(BigInteger, primary_key=True)
    date_of_birth = Column(Date)
    name = Column(String(255), nullable=False)
    preferred_position = Column(String(255))
    shirt_number = Column(BigInteger)


class Season(Base):
    __tablename__ = 'season'

    id = Column(BigInteger, primary_key=True)
    end_year = Column(Date, nullable=False)
    start_year = Column(Date, nullable=False)


class Team(Base):
    __tablename__ = 'team'

    id = Column(BigInteger, primary_key=True)
    date_founded = Column(Date)
    location = Column(String(255))
    manager = Column(String(255))
    name = Column(String(255), nullable=False)


class LeagueTeam(Base):
    __tablename__ = 'league_team'

    id = Column(BigInteger, primary_key=True)
    date_joined = Column(Date)
    league_id = Column(ForeignKey('league.id'), nullable=False)
    season_id = Column(ForeignKey('season.id'), nullable=False)
    team_id = Column(ForeignKey('team.id'), nullable=False)

    league = relationship('League')
    season = relationship('Season')
    team = relationship('Team')


class TeamPlayer(Base):
    __tablename__ = 'team_player'

    id = Column(BigInteger, primary_key=True)
    date_joined = Column(Date)
    player_id = Column(ForeignKey('player.id'), nullable=False)
    team_id = Column(ForeignKey('team.id'), nullable=False)

    player = relationship('Player')
    team = relationship('Team')


class Fixture(Base):
    __tablename__ = 'fixture'

    __table_args__ = (
        UniqueConstraint('fixture_date', 'away_id', 'home_id', name='fixture_unique'),
    )

    id = Column(BigInteger, primary_key=True)
    away_score = Column(BigInteger)
    fixture_date = Column(Date, nullable=False)
    fixture_time = Column(String(255))
    home_score = Column(BigInteger)
    match_week = Column(BigInteger)
    results = Column(String(255))
    away_id = Column(ForeignKey('league_team.id'), nullable=False)
    home_id = Column(ForeignKey('league_team.id'), nullable=False)

    away = relationship('LeagueTeam', primaryjoin='Fixture.away_id == LeagueTeam.id')
    home = relationship('LeagueTeam', primaryjoin='Fixture.home_id == LeagueTeam.id')

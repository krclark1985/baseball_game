import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Team(db.Model):
    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    mlb_id = db.Column(db.Integer, unique=True, nullable=False)

    def __init__(self, name: str, mlb_id: int):
        self.name = name
        self.mlb_id = mlb_id
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'mlb_id': self.mlb_id,
        }

# Make foreign key link to mlb_id in teams table rather than id?
# Also, consider making team_id non-nullable
class Player(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    primary_position = db.Column(db.String(2), nullable=False)
    average = db.Column(db.Float, nullable=False)
    rbi = db.Column(db.Integer, nullable=False)
    homers = db.Column(db.Integer, nullable=False)

    # Include team_id in here or no, since it's nullable?
    def __init__(self, team_id: int, name: str, primary_position: str, average: float, rbi: int, homers: int):
        self.team_id = team_id
        self.name = name
        self.primary_position = primary_position
        self.average = average
        self.rbi = rbi
        self.homers = homers
    
    def serialize(self):
        return {
            'id': self.id,
            'team_id': self.team_id,
            'name': self.name,
            'primary_position': self.primary_position,
            'average': self.average,
            'rbi': self.rbi,
            'homers': self.homers,
        }
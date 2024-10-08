# from .basemodel import BaseModel
# from ..extensions import db
# import uuid

# class Score(BaseModel):
#     __tablename__ = 'scores'
    
#     # UUID as primary key
#     id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))

#     # Relationships
#     games = db.relationship('Game', back_populates='score')

#     # Foreign key to Player
#     player_id = db.Column(db.String(36), db.ForeignKey('players.id'), nullable=False)
    
#     # Relationships
#     player = db.relationship('Player', back_populates='scores')
    
   
#     wins = db.Column(db.Integer, default=0)
#     losses = db.Column(db.Integer, default=0)
#     draws = db.Column(db.Integer, default=0)
from .basemodel import BaseModel
from ..extensions import db
import uuid

class Score(BaseModel):
    __tablename__ = 'scores'
    
    # UUID as primary key
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    player_id = db.Column(db.String(36), db.ForeignKey('players.id'))
    player = db.relationship('Player', back_populates='scores')
    wins = db.Column(db.Integer, default=0, nullable=False)
    losses = db.Column(db.Integer, default=0, nullable=False)
    draws = db.Column(db.Integer, nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'player_id': self.player_id,
            'player': self.player.to_dict() if self.player else None,
            'wins': self.wins,
            'losses': self.losses,
            'draws': self.draws
        }
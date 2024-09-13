# from .basemodel import BaseModel
# from ..extensions import db
# import uuid

# class Game(BaseModel):
#     __tablename__ = 'games'
    
#     # UUID as primary key
#     id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))

#     # Foreign key for one-to-many relationship: Each game is associated with one player
#     player_id = db.Column(db.String(36), db.ForeignKey('players.id'))
#     player = db.relationship('Player', back_populates='games')

#     # Foreign key for one-to-many relationship with score
#     score_id = db.Column(db.String(36), db.ForeignKey('scores.id'))
#     score = db.relationship('Score', back_populates='games')

#     # Many-to-many relationship with Player through association table
#     players = db.relationship('Player', secondary='player_game', back_populates='played_games')
    
#     result = db.Column(db.String(10))

#     def __init__(self, result):
#         self.result = result

from .basemodel import BaseModel
from sqlalchemy.orm import relationship
from .associations import player_game_association 
from ..extensions import db
import uuid

class Game(BaseModel):
    __tablename__ = 'games'
    
    # UUID as primary key
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    result = db.Column(db.String(10))
    # Foreign key for winner and loser
    winner_id = db.Column(db.String(36), db.ForeignKey('players.id'))
    loser_id = db.Column(db.String(36), db.ForeignKey('players.id'))
    
    winner = db.relationship('Player', foreign_keys=[winner_id], back_populates='games_won')
    loser = db.relationship('Player', foreign_keys=[loser_id], back_populates='games_lost')
    
    
    # Many-to-many relationship with Player through association table
    players = db.relationship('Player', secondary=player_game_association, overlaps='played_games')
   
    def to_dict(self):
        return {
            'id': self.id,
            'result': self.result,
            'winner': self.winner.to_dict() if self.winner else None,
            'loser': self.loser.to_dict() if self.loser else None,
            'players': [player.to_dict() for player in self.players]  # Get player names
        
        }


# from .basemodel import BaseModel
# from ..extensions import db
# import uuid

# # Association table for the many-to-many relationship between Player and Game
# player_game_association = db.Table('player_game',
#     db.Column('player_id', db.String(36), db.ForeignKey('players.id')),
#     db.Column('game_id', db.String(36), db.ForeignKey('games.id')),
#     db.Column('role', db.String(50))  # User-submittable attribute
# )

# class Player(BaseModel):
#     __tablename__ = 'players'
    
#     # UUID as primary key
#     id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
#     name = db.Column(db.String(50), nullable=False)
#     score = db.Column(db.Integer, nullable=False)


#     # One-to-many relationship: One player can have many games
#     games = db.relationship('Game', back_populates='player')

#         # Relationship to scores
#     scores = db.relationship('Score', back_populates='player')

#     # Many-to-many relationship: A player can participate in many games
#     played_games = db.relationship('Game', secondary=player_game_association, back_populates='players')
from .basemodel import BaseModel
from ..extensions import db
from .associations import player_game_association

import uuid

class Player(BaseModel):
    __tablename__ = 'players'
    
    # UUID as primary key
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(50), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    
    
    # Relationship to scores
    scores = db.relationship('Score', back_populates='player')
    
    # Many-to-many relationship: A player can participate in many games
    played_games = db.relationship('Game', secondary='player_game', back_populates='players')
    
    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "score": self.score, 
            # "created_at": self.created_at.isoformat(),
            # "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }
        
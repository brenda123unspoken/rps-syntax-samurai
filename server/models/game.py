from .basemodel import BaseModel
from ..extensions import db
import uuid

class Game(BaseModel):
    __tablename__ = 'games'
    
    # UUID as primary key
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))

    # Foreign key for one-to-many relationship: Each game is associated with one player
    player_id = db.Column(db.String(36), db.ForeignKey('players.id'))
    player = db.relationship('Player', back_populates='games')

    # Foreign key for one-to-many relationship with score
    score_id = db.Column(db.String(36), db.ForeignKey('scores.id'))
    score = db.relationship('Score', back_populates='games')

    # Many-to-many relationship with Player through association table
    players = db.relationship('Player', secondary='player_game', back_populates='played_games')
    
    result = db.Column(db.String(10))

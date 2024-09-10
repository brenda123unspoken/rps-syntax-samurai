from .basemodel import BaseModel
from ..extensions import db
import uuid

class Score(BaseModel):
    __tablename__ = 'scores'
    
    # UUID as primary key
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))

    # Relationships
    games = db.relationship('Game', back_populates='score')

    wins = db.Column(db.Integer, default=0)
    losses = db.Column(db.Integer, default=0)
    draws = db.Column(db.Integer, default=0)

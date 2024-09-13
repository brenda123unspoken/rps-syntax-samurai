from ..extensions import db

# Association table for Player and Game with an additional 'role' field
player_game_association = db.Table('player_game_association',
    db.Column('player_id', db.String(36), db.ForeignKey('players.id'), primary_key=True),
    db.Column('game_id', db.String(36), db.ForeignKey('games.id'), primary_key=True),
    db.Column('role', db.String(50))  # Optional: user-submittable attribute
)

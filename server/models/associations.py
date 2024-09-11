from ..extensions import db

player_game_association = db.Table('player_game',
    db.Column('player_id', db.String(36), db.ForeignKey('players.id')),
    db.Column('game_id', db.String(36), db.ForeignKey('games.id')),
    db.Column('role', db.String(50))  # Optional: user-submittable attribute
)

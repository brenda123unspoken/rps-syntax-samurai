from flask import Blueprint, jsonify
from ..models.player import Player

bp = Blueprint('players', __name__, url_prefix='/players')

@bp.route('/')
def get_players():
    players = Player.query.all()
    return jsonify([player.to_dict() for player in players])

class PlayerResource:
    def __init__(self, player_id, name, score):
        self.player_id = player_id
        self.name = name
        self.score = score

    def to_dict(self):
        return {
            "player_id": self.player_id,
            "name": self.name,
            "score": self.score
        }

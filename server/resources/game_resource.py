from flask import Blueprint, jsonify
from models.game import Game

bp = Blueprint('games', __name__, url_prefix='/games')

@bp.route('/')
def get_games():
    games = Game.query.all()
    return jsonify([game.to_dict() for game in games])

class GameResource:
    def __init__(self, game_id):
        self.game_id = game_id

    def to_dict(self):
        # Example method to return a dictionary representation
        return {"game_id": self.game_id}

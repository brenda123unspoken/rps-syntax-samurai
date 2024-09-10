from flask import Blueprint, jsonify
from ..models.score import Score

bp = Blueprint('scores', __name__, url_prefix='/scores')

@bp.route('/')
def get_scores():
    scores = Score.query.all()
    return jsonify([score.to_dict() for score in scores])

class ScoreResource:
    def __init__(self, player_id, score):
        self.player_id = player_id
        self.score = score

    def to_dict(self):
        return {
            "player_id": self.player_id,
            "score": self.score
        }

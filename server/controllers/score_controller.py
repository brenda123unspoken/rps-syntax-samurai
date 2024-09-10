from flask import jsonify
from ..models.score import Score
from ..extensions import cache

@cache.cached(timeout=50, key_prefix='all_scores')
def get_all_scores():
    scores = Score.query.all()
    return jsonify([score.to_dict() for score in scores])

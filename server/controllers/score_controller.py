from flask import jsonify
from ..models.score import Score
from ..extensions import cache, db

@cache.cached(timeout=50, key_prefix='all_scores')

def get_all_scores():
    scores = Score.query.all()
    return jsonify([score.to_dict() for score in scores])

def create_score(data):
    try:
        player_id = data.get('player_id')
        wins = data.get('wins', 0)
        losses = data.get('losses', 0)
        draws = data.get('draws', 0)

        if not player_id or wins is None or losses is None or draws is None:
            return {"error": "player_id, wins, losses, and draws are required"}, 400

        new_score = Score(player_id=player_id, wins=wins, losses=losses, draws=draws)
        db.session.add(new_score)
        db.session.commit()
        return new_score.to_dict(), 201
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 500
       
def get_score(score_id):
    score_id_str = str(score_id)
    score = Score.query.get(score_id_str)
    if not score:
        return {"error": "Score not found"}, 404
    return score.to_dict(), 200

def update_score(score_id, data): 
    score_id_str = str(score_id)
    score = Score.query.get(score_id_str)
    if not score:
        return {"error": "Score not found"}, 404

    score.wins = data.get('wins', score.wins)
    score.losses = data.get('losses', score.losses)
    score.draws = data.get('draws', score.draws)
    db.session.commit()
    return score.to_dict(), 200


def delete_score(score_id):
    score_id_str = str(score_id)
    score = Score.query.get(score_id_str)
    if not score:
        return {"error": "Score not found"}, 404

    db.session.delete(score)
    db.session.commit()
    return {"message": "Score deleted"}, 200
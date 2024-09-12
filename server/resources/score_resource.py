from flask import Blueprint, jsonify, request
from ..controllers.score_controller import get_all_scores, create_score, get_score, update_score, delete_score

bp = Blueprint('scores', __name__, url_prefix='/api/scores')

@bp.route('/', methods=['GET'])
def get_scores():
    return get_all_scores()

@bp.route('/', methods=['POST'])
def create_new_score():
    data = request.get_json()
    response, status_code = create_score(data)
    return jsonify(response), status_code

@bp.route('/<uuid:score_id>', methods=['GET'])
def get_single_score(score_id):
    return get_score(score_id)

@bp.route('/<uuid:score_id>', methods=['PATCH'])
def update_single_score(score_id):
    data = request.get_json()
    response, status_code = update_score(score_id, data)
    return jsonify(response), status_code
@bp.route('/<uuid:score_id>', methods=['DELETE'])
def delete_single_score(score_id):
    response, status_code = delete_score(score_id)
    return jsonify(response), status_code

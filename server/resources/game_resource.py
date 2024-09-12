# # from flask import Blueprint, jsonify
# # from ..models.game import Game

# # bp = Blueprint('games', __name__, url_prefix='/games')

# # @bp.route('/')
# # def get_games():
# #     games = Game.query.all()
# #     return jsonify([game.to_dict() for game in games])

# # class GameResource:
# #     def __init__(self, game_id):
# #         self.game_id = game_id

# #     def to_dict(self):
# #         # Example method to return a dictionary representation
# #         return {"game_id": self.game_id}

# from flask import Blueprint, jsonify
# from ..models.game import Game

# bp = Blueprint('games', __name__, url_prefix='/games')

# @bp.route('/')
# def get_games():
#     games = Game.query.all()
#     return jsonify([game.to_dict() for game in games])

from flask import Blueprint, jsonify, request
from ..controllers.game_controller import get_all_games, create_game, get_game, update_game, delete_game

bp = Blueprint('games', __name__, url_prefix='/api/games')

@bp.route('/', methods=['GET'])
def get_games():
    return get_all_games()

@bp.route('/', methods=['POST'])
def create_new_game():
    data = request.get_json()
    response, status_code = create_game(data)
    return jsonify(response), status_code

@bp.route('/<uuid:game_id>', methods=['GET'])
def get_single_game(game_id):
    response, status_code = get_game(game_id)
    return jsonify(response), status_code

@bp.route('/<uuid:game_id>', methods=['PATCH'])
def update_single_game(game_id):
    data = request.get_json()
    response, status_code = update_game(game_id, data)
    return jsonify(response), status_code

@bp.route('/<uuid:game_id>', methods=['DELETE'])
def delete_single_game(game_id):
    response, status_code = delete_game(game_id)
    return jsonify(response), status_code
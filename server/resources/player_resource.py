# # from flask import Blueprint, jsonify
# # from ..models.player import Player

# # bp = Blueprint('players', __name__, url_prefix='/api/players')

# # @bp.route('/')
# # def get_players():
# #     players = Player.query.all()
# #     return jsonify([player.to_dict() for player in players])

# # class PlayerResource:
# #     def __init__(self, player_id, name, score):
# #         self.player_id = player_id
# #         self.name = name
# #         self.score = score

# #     def to_dict(self):
# #         return {
# #             "player_id": self.player_id,
# #             "name": self.name,
# #             "score": self.score
# #         }
# from flask import Blueprint, jsonify, request
# from ..models.player import Player
# from ..extensions import db, cache

# bp = Blueprint('players', __name__, url_prefix='/api/players')

# @bp.route('/', methods=['GET'])
# def get_players():
#     players = Player.query.all()
#     return jsonify([player.to_dict() for player in players])

# @bp.route('/', methods=['POST'])
# def create_player():
#     data = request.get_json()
#     name = data.get('name')
#     if not name:
#         return jsonify({"error": "Name is required"}), 400
#     player = Player(name=name)
#     db.session.add(player)
#     db.session.commit()
#     cache.delete('all_players')  # Invalidate cache
#     return jsonify(player.to_dict()), 201
from flask import Blueprint, jsonify, request
from ..controllers.player_controller import get_all_players, create_player, get_player, update_player, delete_player

bp = Blueprint('players', __name__, url_prefix='/api/players')

@bp.route('/', methods=['GET'])
def get_players():
    return get_all_players()

@bp.route('/', methods=['POST'])
def create_new_player():
    data = request.get_json()
    response, status_code = create_player(data)
    return jsonify(response), status_code

@bp.route('/<uuid:player_id>', methods=['GET'])
def get_single_player(player_id):
    return get_player(player_id)

@bp.route('/<uuid:player_id>', methods=['PATCH'])
def update_single_player(player_id):
    data = request.get_json()
    response, status_code = update_player(player_id, data)
    return jsonify(response), status_code

@bp.route('/<uuid:player_id>', methods=['DELETE'])
def delete_single_player(player_id):
    response, status_code = delete_player(player_id)
    return jsonify(response), status_code
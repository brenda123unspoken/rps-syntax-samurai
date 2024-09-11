# from flask import jsonify, request
# from ..models.player import Player
# from ..extensions import cache


# @cache.cached(timeout=50, key_prefix='all_players')
# def get_all_players():
#     players = Player.query.all()
#     return jsonify([player.to_dict() for player in players])

# def create_player():
#     data = request.get_json()
#     name = data.get('name')

#     player = Player(name=name)  # UUID is automatically generated
#     player.save()

#     cache.delete('all_players')  # Invalidate cache to refresh list
#     return jsonify(player.to_dict()), 201

from flask import Blueprint, jsonify, request
from ..models.player import Player
from ..extensions import cache

players_bp = Blueprint('players', __name__)

@players_bp.route('/api/players', methods=['GET'])
@cache.cached(timeout=50, key_prefix='all_players')
def get_all_players():
    players = Player.query.all()
    return jsonify([player.to_dict() for player in players])

@players_bp.route('/api/players', methods=['POST'])
def create_player():
    data = request.get_json()
    name = data.get('name')

    if not name:
        return jsonify({"error": "Player name is required"}), 400

    player = Player(name=name)  # UUID is automatically generated
    player.save()

    cache.delete('all_players')  # Invalidate cache to refresh list
    return jsonify(player.to_dict()), 201

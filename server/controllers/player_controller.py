# # from flask import jsonify, request
# # from ..models.player import Player
# # from ..extensions import cache


# # @cache.cached(timeout=50, key_prefix='all_players')
# # def get_all_players():
# #     players = Player.query.all()
# #     return jsonify([player.to_dict() for player in players])

# # def create_player():
# #     data = request.get_json()
# #     name = data.get('name')

# #     player = Player(name=name)  # UUID is automatically generated
# #     player.save()

# #     cache.delete('all_players')  # Invalidate cache to refresh list
# #     return jsonify(player.to_dict()), 201

# from flask import Blueprint, jsonify, request
# from ..models.player import Player
# from ..extensions import cache

# players_bp = Blueprint('players', __name__)

# @players_bp.route('/api/players', methods=['GET'])
# @cache.cached(timeout=50, key_prefix='all_players')
# def get_all_players():
#     players = Player.query.all()
#     return jsonify([player.to_dict() for player in players])

# @players_bp.route('/api/players', methods=['POST'])
# def create_player():
#     data = request.get_json()
#     name = data.get('name')

#     if not name:
#         return jsonify({"error": "Player name is required"}), 400

#     player = Player(name=name)  # UUID is automatically generated
#     player.save()

#     cache.delete('all_players')  # Invalidate cache to refresh list
#     return jsonify(player.to_dict()), 201
from flask import jsonify
from ..models.player import Player
from ..extensions import db, cache

@cache.cached(timeout=50, key_prefix='all_players')
def get_all_players():
    players = Player.query.all()
    return jsonify([player.to_dict() for player in players])

def create_player(data):
    name = data.get('name')
    if not name:
        return {"error": "Name is required"}, 400
    
    player = Player(name=name, score=data.get('score', 0))
    db.session.add(player)
    db.session.commit()
    cache.delete('all_players')
    return player.to_dict(), 201

# def get_player(player_id):
#     player = Player.query.get(player_id_str)
#     if player is None:
#         return {"error": "Player not found"}, 404
#     return player.to_dict(), 200

# def update_player(player_id, data):
#     player = Player.query.get(player_id)
#     if player is None:
#         return {"error": "Player not found"}, 404

#     name = data.get('name')
#     score = data.get('score')

#     if name is not None:
#         player.name = name
#     if score is not None:
#         player.score = score
#         db.session.commit()
#     return player.to_dict(), 200

# def delete_player(player_id):
#     player = Player.query.get(player_id)
#     if player is None:
#         return {"error": "Player not found"}, 404

#     db.session.delete(player)
#     db.session.commit()
#     return {"message": "Player deleted"}, 200
def get_player(player_id):
    player_id_str = str(player_id)  # Convert UUID to string
    player = Player.query.get(player_id_str)
    if player is None:
        return {"error": "Player not found"}, 404
    return player.to_dict(), 200
def update_player(player_id, data):
    player_id_str = str(player_id)  # Convert UUID to string
    player = Player.query.get(player_id_str)
    if player is None:
        return {"error": "Player not found"}, 404

    name = data.get('name')
    score = data.get('score')

    if name is not None:
        player.name = name
    if score is not None:
        player.score = score
        db.session.commit()
    return player.to_dict(), 200
def delete_player(player_id):
    player_id_str = str(player_id)  # Convert UUID to string
    player = Player.query.get(player_id_str)
    if player is None:
        return {"error": "Player not found"}, 404

    db.session.delete(player)
    db.session.commit()
    return {"message": "Player deleted"}, 200


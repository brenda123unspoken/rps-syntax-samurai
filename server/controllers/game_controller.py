# #    from flask import Blueprint, request, jsonify
# #    from server.models.player import Player
# #    from server.models.game import Game
# #    from server.models.score import Score
# #    from server.extensions import cache
# #    from server.utils.get_user_choice import get_user_choice
# #    from server.utils.determine_winner import determine_winner

# #    game_controller = Blueprint('game_controller', __name__)

# #    @game_controller.route('/api/players', methods=['POST'])
# #    def create_player():
# #        data = request.json
# #        player_name = data.get('name')
# #        if not player_name:
# #            return jsonify({"error": "Player name is required"}), 400
# #        # Create and add player logic here
# #        return jsonify({"message": "Player created"}), 201

# #    @game_controller.route('/api/games', methods=['POST'])
# #    def create_game():
# #        data = request.json
# #        player1_name = data.get('player1_name')
# #        player2_name = data.get('player2_name')
# #        # Create game logic here
# #        return jsonify({"message": "Game created"}), 201

# #    @game_controller.route('/api/scores', methods=['POST'])
# #    def create_score():
# #        data = request.json
# #        player_id = data.get('player_id')
# #        score = data.get('score')
# #        # Create score logic here
# #        return jsonify({"message": "Score created"}), 201
# from flask import jsonify, request
# from ..models.game import Game

# from ..extensions import db, cache

# @cache.cached(timeout=50, key_prefix='all_games')
# def get_all_games():
#     games = Game.query.all()
#     return jsonify([game.to_dict() for game in games])

# def create_game():
#     data = request.get_json()

#     player_ids = data.get('player_ids')  # A list of player UUIDs
#     player_roles = data.get('roles')  # Roles of the players (optional)

#     # Create a new game instance
#     game = Game(result="pending")  # This can be updated later with the result

#     # Add the players to the game
#     for i, player_id in enumerate(player_ids):
#         player = Player.query.get(player_id)
#         if player:
#             # Add player and role to the many-to-many relationship
#             game.players.append(player)
#             db.session.execute(
#                 player_game_association.insert().values(player_id=player.id, game_id=game.id, role=player_roles[i])
#             )

#     db.session.add(game)
#     db.session.commit()

#     # Invalidate cache to refresh list of games
#     cache.delete('all_games')

#     return jsonify(game.to_dict()), 201
from flask import jsonify, request
from ..models.game import Game
from ..extensions import db, cache
from ..models.player import Player
from ..models.associations import player_game_association
from ..services.game_service import play_game

# @cache.cached(timeout=50, key_prefix='all_games')
# def get_all_games():
#     games = Game.query.all()
#     return jsonify([game.to_dict() for game in games])

# def create_game(data):
#     player_ids = data.get('player_ids')
#     player_roles = data.get('roles', [])

#     game = Game(result="pending")
#     for i, player_id in enumerate(player_ids):
#         player = Player.query.get(player_id)
#         if player:
#             game.players.append(player)
#             db.session.execute(
#                 player_game_association.insert().values(player_id=player.id, game_id=game.id, role=player_roles[i])
#             )

#     db.session.add(game)
#     db.session.commit()
#     cache.delete('all_games')

#     return game.to_dict(), 201

# def get_game(game_id):
#     game = Game.query.get(str(game_id))
#     if not game:
#         return {"error": "Game not found"}, 404
#     return game.to_dict(), 200

# def update_game(game_id, data):
#     game = Game.query.get(str(game_id))
#     if not game:
#         return {"error": "Game not found"}, 404

#     game.result = data.get('result', game.result)
#     db.session.commit()
#     return game.to_dict(), 200

# def delete_game(game_id):
#     game = Game.query.get(str(game_id))
#     if not game:
#         return {"error": "Game not found"}, 404

#     db.session.delete(game)
#     db.session.commit()
#     cache.delete('all_games')
#     return {"message": "Game deleted"}, 200
# Retrieve all games with caching

@cache.cached(timeout=50, key_prefix='all_games')
def get_all_games():
    games = Game.query.all()
    return jsonify([game.to_dict() for game in games]), 200

# Create a new game and handle associations with players
def create_game(data):
    player_ids = data.get('player_ids')  # List of player IDs
    player_roles = data.get('roles', [])  # Optional list of player roles

    if not player_ids or len(player_ids) < 2:
        return {"error": "At least two players are required to start a game"}, 400

    game = Game(result="pending")
     # Iterate through player_ids and add players to the game
    for i, player_id in enumerate(player_ids):
        player = Player.query.get(player_id)
        if player:
            game.players.append(player)
            # Associate players with the game and roles if provided
            db.session.execute(
                player_game_association.insert().values(
                    player_id=player.id,
                    game_id=game.id,
                    role=player_roles[i] if i < len(player_roles) else None  # Handle missing roles
                )
            )
        else:
            return {"error": f"Player with ID {player_id} not found"}, 404# Commit the new game to the database
    db.session.add(game)
    db.session.commit()

    # Clear cache for all games after creating a new one
    cache.delete('all_games')

    return jsonify(game.to_dict()), 201

# Get a specific game by its ID
def get_game(game_id):
    game = Game.query.get(str(game_id))
    if not game:
        return {"error": "Game not found"}, 404
    return jsonify(game.to_dict()), 200
    # Update the result of a specific game
def update_game(game_id, data):
    game = Game.query.get(str(game_id))
    if not game:
        return {"error": "Game not found"}, 404

    game.result = data.get('result', game.result)  # Update the result if provided
    db.session.commit()

    return jsonify(game.to_dict()), 200

# Delete a game by its ID
def delete_game(game_id):
    game = Game.query.get(str(game_id))
    if not game:
        return {"error": "Game not found"}, 404
        db.session.delete(game)
    db.session.commit()

    # Clear cache for all games after deleting one
    cache.delete('all_games')

    return {"message": "Game deleted"}, 200
    # Play a game and handle logic
def play_game_route():
    data = request.get_json()
    player1_name = data.get('player1_name')
    player2_name = data.get('player2_name')
    player1_choice = data.get('player1_choice')
    player2_choice = data.get('player2_choice')

    # Fetch or create the players
    player1 = get_or_create_player(player1_name)
    player2 = get_or_create_player(player2_name)
# Call the game service function
    game_result = play_game(player1, player2, player1_choice, player2_choice)
    
    return jsonify(game_result), 200

# Helper function to get or create a player
def get_or_create_player(name):
    player = Player.query.filter_by(name=name).first()
    if player is None:
        player = Player(name=name)
        db.session.add(player)
        db.session.commit()
    return player
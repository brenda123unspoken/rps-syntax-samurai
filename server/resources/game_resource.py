# # # from flask import Blueprint, jsonify
# # # from ..models.game import Game

# # # bp = Blueprint('games', __name__, url_prefix='/games')

# # # @bp.route('/')
# # # def get_games():
# # #     games = Game.query.all()
# # #     return jsonify([game.to_dict() for game in games])

# # # class GameResource:
# # #     def __init__(self, game_id):
# # #         self.game_id = game_id

# # #     def to_dict(self):
# # #         # Example method to return a dictionary representation
# # #         return {"game_id": self.game_id}

# # from flask import Blueprint, jsonify
# # from ..models.game import Game

# # bp = Blueprint('games', __name__, url_prefix='/games')

# # @bp.route('/')
# # def get_games():
# #     games = Game.query.all()
# #     return jsonify([game.to_dict() for game in games])

# from flask import Blueprint, jsonify, request
# from ..controllers.game_controller import get_all_games, create_game, get_game, update_game, delete_game

# bp = Blueprint('games', __name__, url_prefix='/api/games')

# @bp.route('/', methods=['GET'])
# def get_games():
#     return get_all_games()

# @bp.route('/', methods=['POST'])
# def create_new_game():
#     data = request.get_json()
#     response, status_code = create_game(data)
#     return jsonify(response), status_code

# @bp.route('/<uuid:game_id>', methods=['GET'])
# def get_single_game(game_id):
#     response, status_code = get_game(game_id)
#     return jsonify(response), status_code

# @bp.route('/<uuid:game_id>', methods=['PATCH'])
# def update_single_game(game_id):
#     data = request.get_json()
#     response, status_code = update_game(game_id, data)
#     return jsonify(response), status_code

# @bp.route('/<uuid:game_id>', methods=['DELETE'])
# def delete_single_game(game_id):
#     response, status_code = delete_game(game_id)
#     return jsonify(response), status_codefrom flask import Blueprint, request, jsonify
from flask import Blueprint, request, jsonify
from ..models.game import Game
from ..models.player import Player
from ..models.associations import player_game_association
from ..extensions import db, cache
from ..services.game_service import play_game  # Ensure this function handles the game logic

# Create a Blueprint for game-related routes


bp = Blueprint('games', __name__, url_prefix='/api/games')


# Retrieve all games with caching
@bp.route('/', methods=['GET'])
@cache.cached(timeout=50, key_prefix='all_games')
def get_all_games():
    games = Game.query.all()
    return jsonify([game.to_dict() for game in games]), 200

# Create a new game and handle associations with players
@bp.route('/', methods=['POST'])
def create_game():
    data = request.get_json()
    player_ids = data.get('player_ids')  # List of player IDs
    player_roles = data.get('roles', [])  # Optional list of player roles
    return create_game(data)
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
            return {"error": f"Player with ID {player_id} not found"}, 404

    # Commit the new game to the database
    db.session.add(game)
    db.session.commit()

    # Clear cache for all games after creating a new one
    cache.delete('all_games')

    return jsonify(game.to_dict()), 201

# Get a specific game by its ID
@bp.route('/<game_id>', methods=['GET'])
def get_game(game_id):
    game = Game.query.get(str(game_id))
    if not game:
        return {"error": "Game not found"}, 404
    return jsonify(game.to_dict()), 200

# Update the result of a specific game
@bp.route('/<game_id>', methods=['PATCH'])
def update_game(game_id):
    data = request.get_json()
    game = Game.query.get(str(game_id))
    if not game:
        return {"error": "Game not found"}, 404

    game.result = data.get('result', game.result)  # Update the result if provided
    db.session.commit()

    return jsonify(game.to_dict()), 200

# Delete a game by its ID
@bp.route('/<game_id>', methods=['DELETE'])
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
@bp.route('/play', methods=['POST'])
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

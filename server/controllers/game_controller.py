#    from flask import Blueprint, request, jsonify
#    from server.models.player import Player
#    from server.models.game import Game
#    from server.models.score import Score
#    from server.extensions import cache
#    from server.utils.get_user_choice import get_user_choice
#    from server.utils.determine_winner import determine_winner

#    game_controller = Blueprint('game_controller', __name__)

#    @game_controller.route('/api/players', methods=['POST'])
#    def create_player():
#        data = request.json
#        player_name = data.get('name')
#        if not player_name:
#            return jsonify({"error": "Player name is required"}), 400
#        # Create and add player logic here
#        return jsonify({"message": "Player created"}), 201

#    @game_controller.route('/api/games', methods=['POST'])
#    def create_game():
#        data = request.json
#        player1_name = data.get('player1_name')
#        player2_name = data.get('player2_name')
#        # Create game logic here
#        return jsonify({"message": "Game created"}), 201

#    @game_controller.route('/api/scores', methods=['POST'])
#    def create_score():
#        data = request.json
#        player_id = data.get('player_id')
#        score = data.get('score')
#        # Create score logic here
#        return jsonify({"message": "Score created"}), 201
from flask import jsonify, request
from ..models.game import Game

from ..extensions import db, cache

@cache.cached(timeout=50, key_prefix='all_games')
def get_all_games():
    games = Game.query.all()
    return jsonify([game.to_dict() for game in games])

def create_game():
    data = request.get_json()

    player_ids = data.get('player_ids')  # A list of player UUIDs
    player_roles = data.get('roles')  # Roles of the players (optional)

    # Create a new game instance
    game = Game(result="pending")  # This can be updated later with the result

    # Add the players to the game
    for i, player_id in enumerate(player_ids):
        player = Player.query.get(player_id)
        if player:
            # Add player and role to the many-to-many relationship
            game.players.append(player)
            db.session.execute(
                player_game_association.insert().values(player_id=player.id, game_id=game.id, role=player_roles[i])
            )

    db.session.add(game)
    db.session.commit()

    # Invalidate cache to refresh list of games
    cache.delete('all_games')

    return jsonify(game.to_dict()), 201

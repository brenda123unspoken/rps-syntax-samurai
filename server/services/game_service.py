from server.extensions import db
from server.models import Player, Game, Score
from server.utils.get_user_choice import get_user_choice
from server.utils.determine_winner import determine_winner
import random

def play_game(player1_name, player2_name=None):
    # Create or retrieve players
    player1 = get_or_create_player(player1_name)
    player2 = get_or_create_player(player2_name) if player2_name else None
    
    if player2:
        # Two-player mode
        player1_choice = get_user_choice(player1_name)
        player2_choice = get_user_choice(player2_name)
        
        result = determine_winner(player1_choice, player2_choice)
        update_scores(player1, player2, result)
        
        return result

    else:
        # Single-player mode
        player_choice = get_user_choice(player1_name)
        computer_choice = random.randint(0, 2)
        result = determine_winner(player_choice, computer_choice)
        update_scores(player1, None, result)
        
        return result

def get_or_create_player(name):
    player = Player.query.filter_by(name=name).first()
    if not player:
        player = Player(name=name)
        db.session.add(player)
        db.session.commit()
    return player

def update_scores(player1, player2, result):
    if "Player 1 wins!" in result:
        player1.score += 1
    elif "Player 2 wins!" in result and player2:
        player2.score += 1
    
    db.session.commit()

def get_player_score(player_name):
    player = Player.query.filter_by(name=player_name).first()
    return player.score if player else None

# from ..models.game import Game
# from ..models.player import Player
# from ..utils.determine_winner import determine_winner

# def create_game(player_choice, computer_choice):
#     winner = determine_winner(player_choice, computer_choice)
#     game = Game(result=winner)
#     return game

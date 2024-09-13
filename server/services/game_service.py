# from server.extensions import db
# from server.models import Player, Game, Score
# from server.utils.get_user_choice import get_user_choice
# from server.utils.determine_winner import determine_winner
# import random

# # def play_game(player1_name, player2_name=None):
# #     # Create or retrieve players
# #     player1 = get_or_create_player(player1_name)
# #     player2 = get_or_create_player(player2_name) if player2_name else None
    
# #     if player2:
# #         # Two-player mode
# #         player1_choice = get_user_choice(player1_name)
# #         player2_choice = get_user_choice(player2_name)
        
# #         result = determine_winner(player1_choice, player2_choice)
# #         update_scores(player1, player2, result)
        
# #         return result

# #     else:
# #         # Single-player mode
# #         player_choice = get_user_choice(player1_name)
# #         computer_choice = random.randint(0, 2)
# #         result = determine_winner(player_choice, computer_choice)
# #         update_scores(player1, None, result)
        
# #         return result

# # def get_or_create_player(name):
# #     player = Player.query.filter_by(name=name).first()
# #     if not player:
# #         player = Player(name=name)
# #         db.session.add(player)
# #         db.session.commit()
# #     return player

# # def update_scores(player1, player2, result):
# #     if "Player 1 wins!" in result:
# #         player1.score += 1
# #     elif "Player 2 wins!" in result and player2:
# #         player2.score += 1
    
# #     db.session.commit()

# # def get_player_score(player_name):
# #     player = Player.query.filter_by(name=player_name).first()
# #     return player.score if player else None

# # # from ..models.game import Game
# # # from ..models.player import Player
# # # from ..utils.determine_winner import determine_winner

# # # def create_game(player_choice, computer_choice):
# # #     winner = determine_winner(player_choice, computer_choice)
# # #     game = Game(result=winner)
# # #     return game

# # def play_game(player1, player2, player1_choice, player2_choice):
# #     # Determine the winner and loser using a utility function
# #     winner_choice, loser_choice = determine_winner(player1_choice, player2_choice)
    
# #     if winner_choice == player1_choice:
# #         winner_player = player1
# #         loser_player = player2
# #         result = f'{player1.name} wins!'
# #         player1.score += 1
    
# #     elif winner == player2_choice:
# #         winner_player = player2
# #         loser_player = player1
# #         result = f'{player2.name} wins!'
# #         player2.score += 1
# #     else:
# #         winner_player = None
# #         loser_player = None
# #         result = "It's a draw!"
# #     # Create a new game entry
# #     game = Game(
# #         result=result,
# #         winner_id=winner_player.id if winner_player else None,
# #         loser_id=loser_player.id if loser_player else None
# #     )
    
# #     # Add players to the game
# #     if player1:
# #     game.players.append(player1)
# #     if player2:
# #     game.players.append(player2)
    
   
    
# #     # Save the game result in the database
# #     db.session.add(game)
# #     db.session.commit()
# #     except Exception as e:
# #         db.session.rollback()
# #         print(f"An error occurred while saving the game: {e}")
# #         return {"error": "An error occurred while saving the game."}


# #     return game.to_dict()
# def update_player_game_associations(player_ids, game_id):
#     for player_id in player_ids:
#         association_entry = player_game_association.insert().values(
#             player_id=player_id,
#             game_id=game_id
#         )
#         db.session.execute(association_entry)
    
#     db.session.commit()
#  def update_scores(winner_id, loser_id):
#     # Update winner's score
#     winner_score = Score.query.filter_by(player_id=winner_id).first()
#     if winner_score:
#         winner_score.wins += 1
    
#     # Update loser's score
#     loser_score = Score.query.filter_by(player_id=loser_id).first()
#     if loser_score:
#         loser_score.losses += 1
    
#     db.session.commit()
#     def record_game_result(player1_id, player2_id, winner_id, loser_id, result):
#     # Create a new Game record
#     game = Game(
#         result=result,
#         winner_id=winner_id,
#         loser_id=loser_id
#     )
    
#     # Add the game to the database
#     db.session.add(game)
#     db.session.commit()
    
#     return game.id

# def play_game(player1, player2, player1_choice, player2_choice):
#     # Determine the winner and loser
#     winner_choice, loser_choice = determine_winner(player1_choice, player2_choice)
    
#     winner_player = None
#     loser_player = None
#     result = "It's a draw!"
    
#     if winner_choice == player1_choice:
#         winner_player = player1
#         loser_player = player2
#         result = f'{player1.name} wins!'
#         player1.score += 1
#     elif winner_choice == player2_choice:
#         winner_player = player2
#         loser_player = player1
#         result = f'{player2.name} wins!'
#         player2.score += 1
    
#     # Record the game result and get the game ID
#     game_id = record_game_result(
#         player1_id=player1.id,
#         player2_id=player2.id if player2 else None,
#         winner_id=winner_player.id if winner_player else None,
#         loser_id=loser_player.id if loser_player else None,
#         result=result
#     )
    
#     # Update scores
#     update_scores(
#         winner_id=winner_player.id if winner_player else None,
#         loser_id=loser_player.id if loser_player else None
#     )
    
#     # Update player-game associations
#     update_player_game_associations([player1.id, player2.id] if player2 else [player1.id], game_id)
    
#     return {
#         "result": result,
#         "game_id": game_id
#     }
from server.extensions import db
from server.models import Player, Game, Score
from server.utils.get_user_choice import get_user_choice
from server.utils.determine_winner import determine_winner
import random

def record_game_result(player1_id, player2_id, winner_id, loser_id, result):
    try:
        game = Game(
            result=result,
            winner_id=winner_id,
            loser_id=loser_id
        )
        db.session.add(game)
        db.session.commit()
        return game.id
    except Exception as e:
        db.session.rollback()
        print(f"An error occurred while recording the game result: {e}")
        return None

def update_scores(winner_id, loser_id):
    try:
        if winner_id:
            winner_score = Score.query.filter_by(player_id=winner_id).first()
            if winner_score:
                winner_score.wins += 1
            else:
                # Create a new Score record if not exists
                new_score = Score(player_id=winner_id, wins=1)
                db.session.add(new_score)
        
        if loser_id:
            loser_score = Score.query.filter_by(player_id=loser_id).first()
            if loser_score:
                loser_score.losses += 1
        else:
                # Create a new Score record if not exists
                new_score = Score(player_id=loser_id, losses=1)
                db.session.add(new_score)
        
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"An error occurred while updating scores: {e}")

def update_player_game_associations(player_ids, game_id):
    try:
        for player_id in player_ids:
            association_entry = player_game_association.insert().values(
                player_id=player_id,
                game_id=game_id
            )
            db.session.execute(association_entry)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"An error occurred while updating player-game associations: {e}")

def play_game(player1, player2, player1_choice, player2_choice):
    try:
        winner_choice, loser_choice = determine_winner(player1_choice, player2_choice)
        
        winner_player = None
        loser_player = None
        result = "It's a draw!"
        
        if winner_choice == player1_choice:
            winner_player = player1
            loser_player = player2
            result = f'{player1.name} wins!'
            player1.score += 1
        elif winner_choice == player2_choice:
            winner_player = player2
            loser_player = player1
            result = f'{player2.name} wins!'
            player2.score += 1
        
        game_id = record_game_result(
            player1_id=player1.id,
            player2_id=player2.id if player2 else None,
            winner_id=winner_player.id if winner_player else None,
            loser_id=loser_player.id if loser_player else None,
            result=result
        )
        
        if game_id:
            update_scores(
                winner_id=winner_player.id if winner_player else None,
                loser_id=loser_player.id if loser_player else None
            )
            update_player_game_associations([player1.id, player2.id] if player2 else [player1.id], game_id)
        
        return {
            "result": result,
            "game_id": game_id
        }
    except Exception as e:
        print(f"An error occurred during the game: {e}")
        return {"error": "An error occurred during the game."}



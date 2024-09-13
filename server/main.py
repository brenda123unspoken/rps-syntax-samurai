# # import random
# from server.utils.determine_winner import determine_winner
# from server.utils.get_user_choice import get_user_choice
# from server.utils.typewriter_effect import typewriter_effect
# from server.models.player import Player
# from server.extensions import db
# from server.app import create_app
# from colorama import init, Fore

# # Initialize colorama for colored outputs
# init()

# # Create the Flask application
# app = create_app()

# def get_or_create_player(name):
#     """Retrieve or create a player based on their name."""
#     player = db.session.query(Player).filter_by(name=name).first()
#     if not player:
#         player = Player(name=name)
#         db.session.add(player)
#         db.session.commit()
#     return player

# def update_score(player, won):
#     """Update the player's score if they win."""
#     if won:
#         player.score += 1
#         db.session.commit()

# def play_game():
#     """Main function to play Rock, Paper, Scissors."""
#     typewriter_effect("Welcome to Rock, Paper, Scissors!")

#     # Ask the user if they want to play against another player or the computer
#     typewriter_effect("Do you want to play with another player or the computer? Type '1' for player or '2' for computer: ")
#     mode = input().strip()

#     if mode == '1':
#         # Get names of Player 1 and Player 2
#         player1_name = input("Enter Player 1's name: ").strip()
#         player2_name = input("Enter Player 2's name: ").strip()

#         # Retrieve or create players
#         player1 = get_or_create_player(player1_name)
#         player2 = get_or_create_player(player2_name)

#         # Get choices from both players
#         print(f"{player1_name}, what do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.")
#         player1_choice = get_user_choice(player1_name)
#         print("\n" * 50)  # Clear the screen for Player 2's turn

#         print(f"{player2_name}, what do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.")
#         player2_choice = get_user_choice(player2_name)

#         # Determine the winner and display the result
#         result = determine_winner(player1_choice, player2_choice)
#         print(result)

#         # Update the score of the winning player
#         if "Player 1 wins!" in result:
#             update_score(player1, True)
#         elif "Player 2 wins!" in result:
#             update_score(player2, True)

#     elif mode == '2':
#         # Get player's name
#         player_name = input("Enter your name: ").strip()
#         player = get_or_create_player(player_name)

#         # Get player's choice
#         print(f"{player_name}, what do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.")
#         player_choice = get_user_choice(player_name)

#         # Get the computer's choice (random)
#         computer_choice = random.randint(0, 2)
#         game_images = ["Rock", "Paper", "Scissors"]
#         typewriter_effect(f"Computer chose: {game_images[computer_choice]}")
#         print(Fore.YELLOW + game_images[computer_choice])

#         # Determine the winner and display the result
#         result = determine_winner(player_choice, computer_choice)
#         print(result)

#         # Update player's score if they win
#         if "You win!" in result:
#             update_score(player, True)

#     else:
#         # Invalid input handling
#         typewriter_effect(Fore.RED + "Invalid input, please type '1' or '2'.")

#     # Ask the user if they want to play again
#     typewriter_effect("Do you want to play again? Type 'yes' or 'no': ")
#     play_again = input().strip().lower()
#     if play_again == 'yes':
#         play_game()

# if __name__ == "__main__":
#     # Run the game within the Flask application context
#     with app.app_context():
#         play_game()
import random
from server.utils.determine_winner import determine_winner
from server.utils.get_user_choice import get_user_choice
from server.utils.typewriter_effect import typewriter_effect
from server.models.player import Player
from server.extensions import db
from server.app import create_app
from colorama import init, Fore

# Initialize colorama for colored outputs
init()

# Create the Flask application
app = create_app()

def get_or_create_player(name):
    """Retrieve or create a player based on their name."""
    player = db.session.query(Player).filter_by(name=name).first()
    if not player:
        player = Player(name=name)
        db.session.add(player)
        db.session.commit()
    return player

def update_score(player, won):
    """Update the player's score if they win."""
    if won:
        player.score += 1
        db.session.commit()

def play_game():
    """Main function to play Rock, Paper, Scissors."""
    typewriter_effect("Welcome to Rock, Paper, Scissors!")

    # Ask the user if they want to play against another player or the computer
    typewriter_effect("Do you want to play with another player or the computer? Type '1' for player or '2' for computer: ")
    mode = input().strip()

    if mode == '1':
        # Get names of Player 1 and Player 2
        player1_name = input("Enter Player 1's name: ").strip()
        player2_name = input("Enter Player 2's name: ").strip()

        # Retrieve or create players
        player1 = get_or_create_player(player1_name)
        player2 = get_or_create_player(player2_name)

        # Get choices from both players
        print(f"{player1_name}, what do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.")
        player1_choice = get_user_choice(player1_name)
        print("\n" * 50)  # Clear the screen for Player 2's turn

        print(f"{player2_name}, what do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.")
        player2_choice = get_user_choice(player2_name)

        # Determine the winner and display the result
        result = determine_winner(player1_choice, player2_choice)
        print(result)

        # Update the score of the winning player
        if "Player 1 wins!" in result:
            update_score(player1, True)
        elif "Player 2 wins!" in result:
            update_score(player2, True)

    elif mode == '2':
        # Get player's name
        player_name = input("Enter your name: ").strip()
        player = get_or_create_player(player_name)

        # Get player's choice
        print(f"{player_name}, what do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.")
        player_choice = get_user_choice(player_name)

        # Get the computer's choice (random)
        computer_choice = random.randint(0, 2)
        game_images = ["Rock", "Paper", "Scissors"]
        typewriter_effect(f"Computer chose: {game_images[computer_choice]}")
        print(Fore.YELLOW + game_images[computer_choice])

        # Determine the winner and display the result
        result = determine_winner(player_choice, computer_choice)
        print(result)

        # Update player's score if they win
        if "You win!" in result:
            update_score(player, True)

    else:
        # Invalid input handling
        typewriter_effect(Fore.RED + "Invalid input, please type '1' or '2'.")

    # Ask the user if they want to play again
    typewriter_effect("Do you want to play again? Type 'yes' or 'no': ")
    play_again = input().strip().lower()
    if play_again == 'yes':
        play_game()

if __name__ == "__main__":
    # Run the game within the Flask application context
    with app.app_context():
        play_game()

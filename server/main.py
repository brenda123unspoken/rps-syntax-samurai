# # from utils.determine_winner import determine_winner
# # from utils.get_user_choice import get_user_choice
# # from utils.typewriter_effect import typewriter_effect

# # from colorama import init, Fore


# # def play_game():
# #     # Welcome message with typewriter effect
# #     typewriter_effect("Welcome to Rock, Paper, Scissors!")
    
# #     # Get choices from both players
# #     player1_choice = get_user_choice("Player 1")
# #     player2_choice = get_user_choice("Player 2")
    
# #     # Determine the winner
# #     result = determine_winner(player1_choice, player2_choice)
    
# #     # Display the result with typewriter effect
# #     typewriter_effect(result)
    
# # if __name__ == "__main__":
# #     play_game()

# import random
# from .utils.determine_winner import determine_winner
# from .utils.get_user_choice import get_user_choice
# from .utils.typewriter_effect import typewriter_effect
# from .models.player import Player
# from server.extensions import db
# from colorama import init, Fore

# # Initialize colorama
# init()

# def get_or_create_player(name):
#     player = db.session.query(Player).filter_by(name=name).first()
#     if not player:
#         player = Player(name=name)
#         session.add(player)
#         session.commit()
#     return player

# def update_score(player, won):
#     if won:
#         player.score += 1
#     session.commit()

# def play_game():
#     typewriter_effect("Welcome to Rock, Paper, Scissors!")

#     # Ask if the user wants to play with another player or the computer
#     typewriter_effect("Do you want to play with another player or the computer? Type '1' for player or '2' for computer: ")
#     mode = input()

#     if mode == '1':
#         player1_name = input("Enter Player 1's name: ")
#         player2_name = input("Enter Player 2's name: ")

#         player1 = get_or_create_player(player1_name)
#         player2 = get_or_create_player(player2_name)

#         print(f"{player1_name}, what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
#         player1_choice = get_user_choice(player1_name)
#         print("\n" * 50)

#         print(f"{player2_name}, what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
#         player2_choice = get_user_choice(player2_name)

#         result = determine_winner(player1_choice, player2_choice)
#         print(result)

#         if result == "Player 1 wins!":
#             update_score(player1, True)
#         elif result == "Player 2 wins!":
#             update_score(player2, True)

#     elif mode == '2':
#         player_name = input("Enter your name: ")
#         player = get_or_create_player(player_name)

#         print(f"{player_name}, what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
#         player_choice = get_user_choice(player_name)

#         computer_choice = random.randint(0, 2)
#         typewriter_effect(f"Computer chose:")
#         print(Fore.YELLOW + game_images[computer_choice])

#         result = determine_winner(player_choice, computer_choice)
#         print(result)

#         if result == "You win!":
#             update_score(player, True)

#     else:
#         typewriter_effect(Fore.RED + "Invalid input, please type '1' or '2'.")

#     # Ask if the user wants to play again
#     typewriter_effect("Do you want to play again? Type 'yes' or 'no': ")
#     play_again = input().lower()
#     if play_again == 'yes':
#         play_game()

# if __name__ == "__main__":
#     play_game()
import random
from server.utils.determine_winner import determine_winner
from server.utils.get_user_choice import get_user_choice
from server.utils.typewriter_effect import typewriter_effect
from server.models.player import Player
from server.extensions import db
from server.app import create_app
from colorama import init, Fore

# Initialize colorama
init()

# Create the Flask application
app = create_app()

def get_or_create_player(name):
    player = db.session.query(Player).filter_by(name=name).first()
    if not player:
        player = Player(name=name)
        db.session.add(player)
        db.session.commit()
    return player

def update_score(player, won):
    if won:
        player.score += 1
        db.session.commit()

def play_game():
    typewriter_effect("Welcome to Rock, Paper, Scissors!")

    # Ask if the user wants to play with another player or the computer
    typewriter_effect("Do you want to play with another player or the computer? Type '1' for player or '2' for computer: ")
    mode = input().strip()

    if mode == '1':
        player1_name = input("Enter Player 1's name: ").strip()
        player2_name = input("Enter Player 2's name: ").strip()

        player1 = get_or_create_player(player1_name)
        player2 = get_or_create_player(player2_name)

        print(f"{player1_name}, what do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.")
        player1_choice = get_user_choice(player1_name)
        print("\n" * 50)

        print(f"{player2_name}, what do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.")
        player2_choice = get_user_choice(player2_name)

        result = determine_winner(player1_choice, player2_choice)
        print(result)

        if result == "Player 1 wins!":
            update_score(player1, True)
        elif result == "Player 2 wins!":
            update_score(player2, True)

    elif mode == '2':
        player_name = input("Enter your name: ").strip()
        player = get_or_create_player(player_name)

        print(f"{player_name}, what do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.")
        player_choice = get_user_choice(player_name)

        computer_choice = random.randint(0, 2)
        typewriter_effect(f"Computer chose:")
        # Assuming `game_images` is a predefined list or dictionary of images or representations
        game_images = ["Rock", "Paper", "Scissors"]  # Define or load appropriate images
        print(Fore.YELLOW + game_images[computer_choice])

        result = determine_winner(player_choice, computer_choice)
        print(result)

        if result == "You win!":
            update_score(player, True)

    else:
        typewriter_effect(Fore.RED + "Invalid input, please type '1' or '2'.")

    # Ask if the user wants to play again
    typewriter_effect("Do you want to play again? Type 'yes' or 'no': ")
    play_again = input().strip().lower()
    if play_again == 'yes':
        play_game()

if __name__ == "__main__":
    with app.app_context():  # Ensure the application context is used
        play_game()

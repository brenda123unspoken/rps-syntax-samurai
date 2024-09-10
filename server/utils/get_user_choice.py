from colorama import Fore
from .game_images import game_images

def get_user_choice(player):
    while True:
        try:
            choice = int(input(Fore.BLUE + f"{player}, what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
            if choice in [0, 1, 2]:
                print(Fore.YELLOW + game_images[choice])
                return choice
            else:
                print(Fore.RED + "Invalid number, please choose 0, 1, or 2.")
        except ValueError:
            print(Fore.RED + "Invalid input, please enter a number.")

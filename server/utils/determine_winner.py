from colorama import Fore

def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return "It's a draw"
    elif (choice1 == 0 and choice2 == 2) or \
         (choice1 == 1 and choice2 == 0) or \
         (choice1 == 2 and choice2 == 1):
        return Fore.GREEN + "Player 1 wins!"
    else:
        return Fore.GREEN + "Player 2 wins!"

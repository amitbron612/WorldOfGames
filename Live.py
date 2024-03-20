from GuessGame import GuessGame
from MemoryGame import MemoryGame
from CurrencyRouletteGame import CurrencyRouletteGame
from Score import add_score
def welcome(name):
    return "\nHello " + name + " and welcome to the World of Games (WoG).\nHere you can find many cool games to play.\n"
def get_valid_input(prompt, min_value, max_value):
    while True:
        try:
            user_input = int(input(prompt))
            if min_value <= user_input <= max_value:
                return user_input
            else:
                print(f"Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Please enter a valid number only.")
def load_game(name):
    while True:
        print("Please choose a game to play:\n"
              "1. Memory Game - a sequence of numbers will appear for 1 second, and you have to guess it back\n"
              "2. Guess Game - guess a number and see if you chose like the computer\n"
              "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n")
        chosen_game = get_valid_input("Which game would you like: ", 1, 3)
        difficulty = get_valid_input("Choose game difficulty (1-5): ", 1, 5)
        if chosen_game == 1:
            won = MemoryGame(difficulty)
        elif chosen_game == 2:
            won = GuessGame(difficulty)
        elif chosen_game == 3:
            won = CurrencyRouletteGame(difficulty)

        if won:
            print("You Won!")
            add_score(name, difficulty)

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break
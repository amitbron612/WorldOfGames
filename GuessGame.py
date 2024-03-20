import random

def GuessGame(difficulty):
    secret_number = None

    def generate_number(difficulty):
        nonlocal secret_number
        secret_number = random.randint(1, difficulty)

    def get_guess_from_user(difficulty):
        while True:
            try:
                guess = int(input(f"Guess a number between 1 and {difficulty}: "))
                if 1 <= guess <= difficulty:
                    return guess
                else:
                    print(f"Please enter a number between 1 and {difficulty}.")
            except ValueError:
                print("Please enter a valid integer.")

    def compare_results(user_guess):
        if user_guess == secret_number:
            print("Congratulations! You guessed the correct number!")
            return True
        else:
            print(f"Sorry, you guessed the wrong number. The Number Was: {secret_number} ")
            return False

    difficulty = int(difficulty)
    generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    return compare_results(user_guess)

# Example usage:
if __name__ == "__main__":
    difficulty = input("Enter game difficulty (1-5): ")
    GuessGame(difficulty)

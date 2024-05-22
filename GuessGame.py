import random

class GuessGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.secret_number = None

    def generate_number(self):
        self.secret_number = random.randint(1, self.difficulty)
        return self.secret_number

    def compare_results(self, guess, secret_number):
        return guess == secret_number

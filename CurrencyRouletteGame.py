import random
import requests

class CurrencyRouletteGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.exchange_rate = self.get_exchange_rate()
        self.generated_number = self.generate_number()

    def get_exchange_rate(self):
        response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
        data = response.json()
        return data['rates']['ILS']

    def generate_number(self):
        return random.randint(1, 100)

    def get_money_interval(self):
        total_value_of_money = self.generated_number * self.exchange_rate
        lower_bound = total_value_of_money - (5 - self.difficulty)
        upper_bound = total_value_of_money + (5 - self.difficulty)
        return lower_bound, upper_bound

    def play(self, user_guess):
        lower_bound, upper_bound = self.get_money_interval()
        return lower_bound <= user_guess <= upper_bound, self.generated_number, lower_bound, upper_bound

# Example usage:
if __name__ == "__main__":
    difficulty = int(input("Enter game difficulty (1-5): "))
    game = CurrencyRouletteGame(difficulty)
    print(f"Generated number: {game.generated_number}")
    print(f"Exchange rate from USD to ILS: {game.exchange_rate}")
    lower_bound, upper_bound = game.get_money_interval()
    print(f"Interval: [{lower_bound}, {upper_bound}]")
    user_guess = float(input("Guess the value of the generated number in USD after exchange to ILS: "))
    result, _, _, _ = game.play(user_guess)
    if result:
        print("Congratulations! Your guess is correct!")
    else:
        print("Sorry, your guess is incorrect. You lost.")

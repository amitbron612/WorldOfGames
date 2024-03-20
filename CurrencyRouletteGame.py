import random
import requests


def get_exchange_rate():
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    data = response.json()
    return data['rates']['ILS']


def generate_number():
    return random.randint(1, 100)


def get_money_interval(difficulty, generated_number, exchange_rate):
    total_value_of_money = generated_number * exchange_rate
    lower_bound = total_value_of_money - (5 - difficulty)
    upper_bound = total_value_of_money + (5 - difficulty)
    return lower_bound, upper_bound


def get_guess_from_user():
    while True:
        try:
            guess = float(input("Guess the value of the generated number in USD after exchange to ILS: "))
            return guess
        except ValueError:
            print("Please enter a valid number.")


def CurrencyRouletteGame(difficulty):
    exchange_rate = get_exchange_rate()
    generated_number = generate_number()

    print(f"Generated number: {generated_number}")
    print(f"Exchange rate from USD to ILS: {exchange_rate}")

    lower_bound, upper_bound = get_money_interval(difficulty, generated_number, exchange_rate)
    # print(f"Interval: [{lower_bound}, {upper_bound}]")

    user_guess = get_guess_from_user()
    print(f"User's guess: {user_guess}")

    if lower_bound <= user_guess <= upper_bound:
        print("Congratulations! Your guess is correct!")
        return True
    else:
        print("Sorry, your guess is incorrect. You lost.")
        return False


# Example usage:
if __name__ == "__main__":
    difficulty = int(input("Enter game difficulty (1-5): "))
    CurrencyRouletteGame(difficulty)

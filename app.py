from flask import Flask, render_template, request, redirect, url_for, session
from MemoryGame import MemoryGame
from GuessGame import GuessGame
from CurrencyRouletteGame import CurrencyRouletteGame
from Score import add_score, get_all_scores
import os
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key
def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv('MYSQL_HOST', 'db'),
        user=os.getenv('MYSQL_USER', 'root'),
        password=os.getenv('MYSQL_PASSWORD', 'password'),
        database=os.getenv('MYSQL_DATABASE', 'games')
    )
@app.route('/')
def welcome_page():
    return render_template('welcome.html')

@app.route('/gamepicker', methods=['GET', 'POST'])
def game_picker():
    if request.method == 'POST':
        name = request.form['name']
        chosen_game = int(request.form['game'])
        difficulty = int(request.form['difficulty'])

        session['name'] = name
        session['chosen_game'] = chosen_game
        session['difficulty'] = difficulty

        if chosen_game == 1:
            return redirect(url_for('memory_game'))
        elif chosen_game == 2:
            return redirect(url_for('guess_game'))
        elif chosen_game == 3:
            return redirect(url_for('currency_roulette_game'))

    return render_template('game_picker.html')

@app.route('/MemoryGame', methods=['GET', 'POST'])
def memory_game():
    if request.method == 'GET':
        difficulty = session.get('difficulty')
        game = MemoryGame(difficulty)
        sequence = game.generate_sequence()
        session['sequence'] = sequence  # Store the generated sequence in the session
        return render_template('memory_game.html', sequence=sequence, difficulty=difficulty)

    elif request.method == 'POST':
        difficulty = int(request.form['difficulty'])
        user_list = [int(request.form[f'num_{i+1}']) for i in range(difficulty)]
        sequence = session.get('sequence')  # Retrieve the sequence from the session
        game = MemoryGame(difficulty, sequence)
        result, correct_sequence = game.play(user_list)
        name = session.get('name')

        if result:
            add_score(name, difficulty)
            return render_template('memory_game_result.html', result="Congratulations! You remembered all the numbers!", sequence=correct_sequence)
        else:
            return render_template('memory_game_result.html', result="Sorry, you did not remember all the numbers. You lost.", sequence=correct_sequence)

@app.route('/GuessGame', methods=['GET', 'POST'])
def guess_game():
    if request.method == 'GET':
        return render_template('guess_game.html')

    elif request.method == 'POST':
        difficulty = session.get('difficulty')
        game = GuessGame(difficulty)
        secret_number = game.generate_number()
        user_guess = int(request.form['guess'])
        game.secret_number = secret_number  # Ensure the correct secret number is set
        result = game.play(user_guess)
        name = session.get('name')

        if result:
            add_score(name, difficulty)
            return render_template('guess_game_result.html', result="Congratulations! You guessed the number!", secret_number=secret_number)
        else:
            return render_template('guess_game_result.html', result="Sorry, your guess is incorrect. You lost.", secret_number=secret_number)

@app.route('/CurrencyRouletteGame', methods=['GET', 'POST'])
def currency_roulette_game():
    if request.method == 'GET':
        difficulty = session.get('difficulty')
        game = CurrencyRouletteGame(difficulty)
        session['generated_number'] = game.generated_number
        session['exchange_rate'] = game.exchange_rate
        return render_template('currency_roulette_game.html', difficulty=difficulty, generated_number=game.generated_number)

    elif request.method == 'POST':
        difficulty = session.get('difficulty')
        generated_number = session.get('generated_number')
        exchange_rate = session.get('exchange_rate')
        user_guess = float(request.form['guess'])

        game = CurrencyRouletteGame(difficulty)
        game.generated_number = generated_number
        game.exchange_rate = exchange_rate

        result, _, lower_bound, upper_bound = game.play(user_guess)
        name = session.get('name')

        if result:
            add_score(name, difficulty)
            return render_template('currency_roulette_result.html', result="Congratulations! Your guess is correct!", lower_bound=lower_bound, upper_bound=upper_bound, guess=user_guess)
        else:
            return render_template('currency_roulette_result.html', result="Sorry, your guess is incorrect. You lost.", lower_bound=lower_bound, upper_bound=upper_bound, guess=user_guess)

@app.route('/scoreboard')
def scoreboard():
    scores = get_all_scores()
    return render_template('scoreboard.html', scores=scores)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

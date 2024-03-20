from flask import Flask, render_template
import json

app = Flask(__name__, template_folder='template')

def score_server(name):
    if not isinstance(name, str):
        return "Name must be a string."

    with open('scores.json', 'r') as file:
        scores = json.load(file)

    if name in scores:
        score = scores[name]
        return render_template('score_template.html', SCORE=score)
    else:
        return render_template('name_not_exist.html')

@app.route('/score/<name>')
def get_score(name):
    return score_server(name)

if __name__ == '__main__':
    app.run(debug=True)

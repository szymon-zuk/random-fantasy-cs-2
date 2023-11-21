from flask import Flask, render_template, jsonify
from scrap import generate_random_team
import random


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/draw', methods=['POST'])
def draw():
    generated_team = generate_random_team()
    names = [player[0] for player in generated_team]
    total_cost = sum(player[1] for player in generated_team)
    return jsonify({'success': True, 'generated_team': generated_team, 'total_cost': total_cost})

if __name__ == '__main__':
    app.run(debug=True)

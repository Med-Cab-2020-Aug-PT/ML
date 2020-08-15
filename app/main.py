import random
from flask import Flask, jsonify
import pandas as pd
"""
Input  :: Text? Dropdown Selection? Numeric? 
Output :: type: string, description, list flavors, list effects
"""

__all__ = ('random_recommendation', 'index_route', 'APP')


def load_data():
    return pd.read_csv('cannabis.csv').to_dict(orient='records')


APP = Flask(__name__)
DATA = load_data()


def random_recommendation():
    return random.choice(DATA)


@APP.route('/')
def index_route():
    return jsonify(random_recommendation())


if __name__ == '__main__':
    APP.run()

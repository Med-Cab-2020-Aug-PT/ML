from flask import Flask, jsonify
from app.data import GetData


__all__ = ('APP',)
APP = Flask(__name__)
DATA = GetData(filename='data_sources/cleaned_cannabis.csv')


@APP.route('/')
@APP.route('/index.html')
def index_route():
    return jsonify(DATA.recommendation())


@APP.route('/strain-by-id/<idx>', methods=['GET'])
def strain_by_id(idx: str):
    return jsonify(DATA.strain_by_id(int(idx)))


@APP.route('/strain-by-name/<name>', methods=['GET'])
def strain_by_name(name: str):
    return jsonify(DATA.strain_by_name(name))


if __name__ == '__main__':
    APP.run()

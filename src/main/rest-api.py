from flask import Flask, jsonify, request
from weather import db, Weather
import os, json
app = Flask(__name__)


@app.before_request
def before_request():
    with open(os.path.dirname(os.path.realpath(__file__)) + "\\db-config.json") as db_config_file:
        db_config = json.load(db_config_file)
    db.init(db_config['db-name'],
            user=db_config['user'],
            password=db_config['password'],
            host=db_config['host'],
            port=db_config['port'])
    db.connect()


@app.after_request
def after_request(response):
    db.close()
    return response


@app.route('/')
def hello_world():
    return 'Hello World!!'


@app.route('/weather')
def weather_service():
    return jsonify(Weather
                   .select()
                   .where(Weather.date == request.args.get('day'))
                   .get()
                   .serialize())

from flask import Flask, jsonify
from .trained_ai import LoadedModel

real = LoadedModel.return_object

test = {
        "name": "PETR4",
        "values":{
            "real": [2, 3, 6, 8, None, None, None],
            "test": [3, 4, 5, 7, None, None, None],
            "prediction": [None, None, None, 8, 9, 10, 7],
            "date": ["2021-04-05", "2021-04-06", "2021-04-07", "2021-04-08", "2021-04-09", "2021-04-10", "2021-04-11"]
        }
    }

def create_app():
    app = Flask(__name__)
    
    @app.route('/test')
    def predictions():
        return jsonify(test)

    @app.route('/')
    def home():
        return jsonify(real)

    return app


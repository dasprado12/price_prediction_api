from flask import Flask, jsonify
from .trained_ai import LoadedModel
from flask_cors import CORS, cross_origin

testModel = LoadedModel()

app = Flask(__name__)
CORS(app)

test = {
        "name": "PETR4",
        "values":{
            "real": [2, 3, 6, 8, None, None, None],
            "test": [3, 4, 5, 7, None, None, None],
            "prediction": [None, None, None, 8, 9, 10, 7],
            "date": ["2021-04-05", "2021-04-06", "2021-04-07", "2021-04-08", "2021-04-09", "2021-04-10", "2021-04-11"]
        }
    }
helloWorld = {
    "mensage":"Hello world"
}

def create_app():
    app = Flask(__name__)
    
    @app.route('/')
    @cross_origin(origin='*')
    def HelloWorld():
        return jsonify(helloWorld)

    @app.route('/test')
    @cross_origin(origin='*')
    def predictions():
        return jsonify(test)

    @app.route('/PETR4')
    @cross_origin(origin='*')
    def petr4():
        result = testModel.SetParameters("PETR4")
        return jsonify(result)
    
    @app.route('/AMBEV')
    @cross_origin(origin='*')
    def ambev():
        result = testModel.SetParameters("AMBEV")
        return jsonify(result)
    
    @app.route('/CIELO')
    @cross_origin(origin='*')
    def cielo():
        result = testModel.SetParameters("CIELO")
        return jsonify(result)
    
    @app.route('/ITAU')
    @cross_origin(origin='*')
    def itau():
        result = testModel.SetParameters("ITAU")
        return jsonify(result)

    return app


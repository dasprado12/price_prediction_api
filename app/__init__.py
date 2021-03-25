from flask import Flask, jsonify
from .trained_ai import LoadedModel

real = LoadedModel.close_test.tolist()


def create_app():
    app = Flask(__name__)
    
    @app.route('/')
    def home():
        return jsonify(real)

    return app
from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)
    
    @app.route('/')
    def home():
        return jsonify({'message': 'The API is running'})

    return app
from flask import Flask
from flask_cors import CORS
from app.routes import init_app

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config["PROPAGATE_EXCEPTIONS"] = True
    init_app(app)
    return app
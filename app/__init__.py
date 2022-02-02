from flask import Flask

from app.routes import init_app

def create_app():
    app = Flask(__name__)
    app.config["PROPAGATE_EXCEPTIONS"] = True
    init_app(app)
    return app
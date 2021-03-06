from flask import Flask
from app.controllers import servers

def create_app():
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.register_blueprint(servers.bp, url_prefix="/servers")

    return app


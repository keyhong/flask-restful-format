"""TODO"""

import logging
import os

from api.demo_api import blp_v1 as APIBlueprint
from db import db
from flask import Flask
from flask_smorest import Api

logger = logging.getLogger(__name__)

def create_app(db_url=None) -> Flask:
    """TODO"""

    app = Flask(__name__)

    app.config["API_TITLE"] = "Demo Flask Restful API Format"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True

    db.init_app(app)

    with app.app_context():
        db.create_all()

    api = Api(app)
    api.register_blueprint(APIBlueprint)

    api.init_app(app)

    return app


class MyApp(Flask):
    """TODO"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    from controllers.atividade_controller import atividade_bp
    app.register_blueprint(atividade_bp, url_prefix="/atividades")

    with app.app_context():
        db.create_all()

    return app

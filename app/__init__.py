from flask import Flask, jsonify
from flasgger import Swagger
from .extensions import db
from .config import DATABASE_URI, TRACK_MODIFICATIONS
from .controllers.atividade_controller import atividade_bp  # Descomentado

def create_app():
    app = Flask(__name__)

    # Configurações
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = TRACK_MODIFICATIONS
    app.config["SWAGGER"] = {
        "title": "Atividades API - Documentação com Swagger",
        "uiversion": 3
    }

    # Inicializa extensões
    db.init_app(app)
    Swagger(app)

    # Registrar rotas
    @app.route("/")
    def home():
        return jsonify({"mensagem": "Bem-vindo à API de Atividades! Documentação: /apidocs/"})

    app.register_blueprint(atividade_bp, url_prefix="/atividades")  # Registra o blueprint

    # Cria as tabelas no banco
    with app.app_context():
        db.create_all()

    return app
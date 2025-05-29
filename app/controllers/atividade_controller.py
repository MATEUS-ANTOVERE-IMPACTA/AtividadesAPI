from flask import Blueprint, jsonify, request
from app.models.atividade import Atividade
from app.extensions import db

atividade_bp = Blueprint("atividade", __name__)

@atividade_bp.route("/", methods=["GET"])
def listar():
    atividades = Atividade.query.all()
    return jsonify([a.to_dict() for a in atividades]), 200

@atividade_bp.route("/", methods=["POST"])
def criar():
    data = request.get_json()

    if not data or "titulo" not in data or "descricao" not in data or "professor_id" not in data:
        return jsonify({"erro": "Campos obrigatórios: titulo, descricao, professor_id"}), 400

    atividade = Atividade(
        titulo=data["titulo"],
        descricao=data["descricao"],
        professor_id=data["professor_id"]
    )

    db.session.add(atividade)
    db.session.commit()
    return jsonify(atividade.to_dict()), 201
from flask import Blueprint, request, jsonify
from app.models.atividade import Atividade

atividade_bp = Blueprint('atividade_bp', __name__)

@atividade_bp.route('', methods=['GET'])
def listar_atividades():
    return jsonify(Atividade.listar())

@atividade_bp.route('', methods=['POST'])
def criar_atividade():
    data = request.get_json()
    resposta, status = Atividade.criar(data)
    return jsonify(resposta), status

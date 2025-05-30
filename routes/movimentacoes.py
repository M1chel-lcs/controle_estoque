from flask import Blueprint, request, jsonify
from models.movimentacoes import registrar_movimentacao, gerar_relatorio

movimentacoes_bp = Blueprint('movimentacoes', __name__)

@movimentacoes_bp.route('/movimentacoes', methods=['POST'])
def movimentar_estoque():
    dados = request.get_json()
    registrar_movimentacao(dados)
    return jsonify({'mensagem': f"{dados['tipo']} registrada com sucesso!"})

@movimentacoes_bp.route('/relatorio', methods=['GET'])
def relatorio():
    dados = gerar_relatorio()
    return jsonify(dados)

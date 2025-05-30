from flask import Blueprint, request, render_template, redirect, url_for, flash
from models.produtos import inserir_produto
from models.produtos import listar_produto


produtos_bp = Blueprint('produtos', __name__)

@produtos_bp.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar_produto():
    if request.method == 'POST':
        try:
            dados = {

                'nome': request.form['nome'],
                'categoria': request.form.get('categoria', ''),
                'preco': float(request.form['preco']),
                'quantidade_atual': int(request.form['quantidade']),
                'localizacao': request.form.get('localizacao')
                
            }
            
            inserir_produto(dados)
            flash('Produto cadastrado com sucesso!', 'success')
            return redirect(url_for('produtos.cadastrar_produto'))
       
        except Exception as e:
            flash(f'Erro ao cadastrar: {str(e)}', 'danger')
    
    return render_template('cadastrar_produto.html')

@produtos_bp.route('/estoque')
def visualizar_estoque():
    produtos = listar_produto()
    return render_template('estoque.html', produtos=produtos)
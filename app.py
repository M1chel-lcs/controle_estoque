from flask import Flask, render_template
from routes.produtos import produtos_bp
from routes.movimentacoes import movimentacoes_bp

app = Flask(__name__)
app.secret_key = 'chave-secreta'  
app.register_blueprint(produtos_bp, url_prefix='/produtos')
app.register_blueprint(movimentacoes_bp, url_prefix='/movimentacoes')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/movimentar', methods=['GET'])
def movimentar():
    return render_template('movimentar.html')

@app.route('/relatorio', methods=['GET'])
def relatorio():
    
    relatorio = [] 
    return render_template('relatorio.html', relatorio=relatorio)

if __name__ == '__main__':
    app.run(debug=True)

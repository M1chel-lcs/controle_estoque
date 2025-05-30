from models.db import conectar

def inserir_produto(dados):
    conn = conectar()
    cursor = conn.cursor()
    sql = """ insert into produtos (nome, categoria, preco, quantidade_atual, localizacao) values (%s, %s, %s, %s, %s)"""
    valores = (
        dados['nome'],
        dados['categoria'],
        dados['preco'],
        dados['quantidade_atual'],
        dados['localizacao']  )
    cursor.execute(sql, valores)
    conn.commit()
    cursor.close()
    conn.close()
    
def listar_produto():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, nome, categoria, preco, quantidade_atual, localizacao FROM produtos")
    produtos = cursor.fetchall()
    cursor.close()
    conn.close()
    return produtos

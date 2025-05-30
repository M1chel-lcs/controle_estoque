from models.db import conectar

def registrar_movimentacao(dados):
    conn = conectar()
    cursor = conn.cursor()

    tipo = dados['tipo']
    quantidade = dados['quantidade']
    produto_id = dados['produto_id']

    sql = """insert into movimentacoes (produto_id, tipo, quantidade) value (%s, %s, %s)"""

    cursor.execute(sql, (produto_id, tipo, quantidade))

    if tipo == 'entrada':
        cursor.execute("update produtos set quantidade_atual = quantidade_atual + %s where id = %s", (quantidade, produto_id))
    elif tipo == 'saida':
        cursor.execute("update produtos set quantidade_atual = quanridade_atual - %s where id = %s", (quantidade, produto_id,))

    conn.commit()
    cursor.close()
    conn.close()

def gerar_relatorio():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("select * from relatorio_estoque")
    resultados = cursor.fetchall()
    cursor.close()
    conn.close()
    return resultados

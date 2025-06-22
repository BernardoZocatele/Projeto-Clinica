import eel
from .gerar_banco import conectar
from datetime import datetime

def registrar_log(usuario, item, quantidade, acao, empresa_id):
    conn = conectar()
    cursor = conn.cursor()
    data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('''
        INSERT INTO logs_estoque (usuario, item, quantidade, acao, data_hora, empresa_id)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (usuario, item, quantidade, acao, data_hora, empresa_id))
    conn.commit()
    conn.close()

@eel.expose
def inserir_item(usuario, empresa_id, nome, qtd, minimo):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM estoque WHERE nome = ? AND empresa_id = ?", (nome, empresa_id))
    resultado = cursor.fetchone()

    if resultado:
        cursor.execute("UPDATE estoque SET quantidade = quantidade + ? WHERE nome = ? AND empresa_id = ?", (qtd, nome, empresa_id))
        print("Item atualizado.")
    else:
        cursor.execute("INSERT INTO estoque (nome, quantidade, minimo, empresa_id) VALUES (?, ?, ?, ?)", (nome, qtd, minimo, empresa_id))
        print("Item inserido.")
    conn.commit()
    conn.close()
    registrar_log(usuario, nome, qtd, 'insercao', empresa_id)
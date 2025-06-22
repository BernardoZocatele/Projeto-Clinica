import eel
from .gerar_banco import conectar
from datetime import datetime

def registrar_log(usuario, item, quantidade, acao, empresa_id):
    try:
        with conectar() as conn:
            cursor = conn.cursor()
            data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute('''
                INSERT INTO logs_estoque (usuario, item, quantidade, acao, data_hora, empresa_id)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (usuario, item, quantidade, acao, data_hora, empresa_id))
            conn.commit()
    except Exception as e:
        print(f"Erro ao registrar log: {e}")

@eel.expose
def inserir_item(usuario, empresa_id, nome, qtd, minimo):
    try:
        with conectar() as conn:
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
        registrar_log(usuario, nome, qtd, 'insercao', empresa_id)
    except Exception as e:
        print(f"Erro ao inserir item: {e}")

@eel.expose
def consultar_estoque(empresa_id, nome_filtro):
    try:
        with conectar() as conn:
            cursor = conn.cursor()
            
            if nome_filtro:
                cursor.execute("SELECT nome, quantidade, empresa_id FROM estoque WHERE empresa_id = ? AND nome LIKE ?", (empresa_id, '%' + nome_filtro + '%'))
            else:
                cursor.execute("SELECT nome, quantidade, empresa_id FROM estoque WHERE empresa_id = ?", (empresa_id,))
            
            resultado = cursor.fetchall()
        
        return resultado
    except Exception as e:
        print(f"Erro ao consultar estoque: {e}")
        return []

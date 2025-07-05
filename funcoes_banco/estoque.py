import eel
from .gerar_banco import conectar
from datetime import datetime

def registrar_log(usuario, item, quantidade, acao, empresa_id, conn):
    cursor = conn.cursor()
    data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('''
        INSERT INTO logs_estoque (usuario, item, quantidade, acao, data_hora, empresa_id)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (usuario, item, quantidade, acao, data_hora, empresa_id))

@eel.expose
def inserir_item(usuario, empresa_id, nome, qtd, minimo, id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM estoque WHERE nome = ? AND empresa_id = ?", (nome, empresa_id))
    resultado = cursor.fetchone()

    if resultado:
        eel.mensagem_usuario("Item já cadastrado no estoque.") 
    else:
        cursor.execute("INSERT INTO estoque (nome, quantidade, minimo, empresa_id, id_consulta) VALUES (?, ?, ?, ?, ?)", (nome, qtd, minimo, empresa_id, id))
        conn.commit()
        eel.mensagem_usuario("Item Cadastrado com sucesso.") 
        registrar_log(usuario, nome, qtd, 'insercao', empresa_id, conn)
    
    conn.commit()
    conn.close()

@eel.expose
def consultar_estoque(empresa_id, nome_filtro):
    conn = conectar()    
    cursor = conn.cursor()
            
    if nome_filtro:
        # Consulta de um item especifico
        if nome_filtro.isdigit():
            # Consulta deita por ID do produto
            cursor.execute("SELECT nome, quantidade, id_consulta FROM estoque WHERE empresa_id = ? AND id_consulta = ?", (empresa_id, nome_filtro))
            resultado = cursor.fetchone()
        else:
            # Consulta feita por nome do produto
            cursor.execute("SELECT nome, quantidade, id_consulta FROM estoque WHERE empresa_id = ? AND nome = ?", (empresa_id, nome_filtro))
            resultado = cursor.fetchone()
            
        if resultado:
            eel.receber_estoque(resultado)
        else:
            eel.mensagem_usuario("Item não encontrado no estoque.")
    else:
        # Consulta do estoque inteiro
        cursor.execute("SELECT nome, quantidade, id_consulta FROM estoque WHERE empresa_id = ?", (empresa_id,))
        resultado = cursor.fetchall()
        eel.receber_estoque_todo(resultado)
        
    conn.close()
        

@eel.expose
def editar_item(usuario, empresa_id, nome, qtd, acao):
    conn = conectar()
    cursor = conn.cursor()
    
    if nome.isdigit():
        cursor.execute("SELECT quantidade FROM estoque WHERE id_consulta = ? AND empresa_id = ?", (nome, empresa_id))
        resultado = cursor.fetchone()
    else:
        cursor.execute("SELECT quantidade FROM estoque WHERE nome = ? AND empresa_id = ?", (nome, empresa_id))
        resultado = cursor.fetchone()

    if resultado:
        qtd = int(qtd)
        
        if acao == 1:
            # Ação 1 - Remover item
            atual = resultado[0]
            
            if atual >= qtd:
                if nome.isdigit():
                    cursor.execute("UPDATE estoque SET quantidade = quantidade - ? WHERE id_consulta = ? AND empresa_id = ?", (qtd, nome, empresa_id))
                else:
                    cursor.execute("UPDATE estoque SET quantidade = quantidade - ? WHERE nome = ? AND empresa_id = ?", (qtd, nome, empresa_id))
                registrar_log(usuario, nome, qtd, 'baixa', empresa_id, conn)
                eel.mensagem_usuario("Estoque atualizado com sucesso.") 
            else:
                eel.mensagem_usuario("Quantidade insuficiente no estoque.")
        else:
            # Ação 2 - Adicionar item 
            if nome.isdigit():
                cursor.execute("UPDATE estoque SET quantidade = quantidade + ? WHERE id_consulta = ? AND empresa_id = ?", (qtd, nome, empresa_id))
            else:
                cursor.execute("UPDATE estoque SET quantidade = quantidade + ? WHERE nome = ? AND empresa_id = ?", (qtd, nome, empresa_id))
            registrar_log(usuario, nome, qtd, 'entrada', empresa_id, conn)
            eel.mensagem_usuario("Estoque atualizado com sucesso.") 
    else:
        eel.mensagem_usuario("Item não encontrado no estoque.")
        
    conn.commit()
    conn.close()
        
        
    

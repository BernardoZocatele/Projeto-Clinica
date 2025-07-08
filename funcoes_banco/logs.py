import eel
from .gerar_banco import conectar

@eel.expose
def consultar_log(empresa_id):
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute("SELECT usuario, item, quantidade, acao, data_hora FROM logs_estoque WHERE empresa_id = ?", (empresa_id, ))
    resultado = cursor.fetchall()
    
    eel.receber_logs(resultado)
    
    cursor.close()
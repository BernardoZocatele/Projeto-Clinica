import sqlite3
import eel
from .gerar_banco import conectar
from criptografia.hashe import hash_password, check_password

@eel.expose
def cadastrar_usuario(nome, login, senha, empresa, is_admin):
    conn = conectar()
    cursor = conn.cursor()
    
    hashed_password = hash_password(senha)
    
    print(is_admin)

    cursor.execute("""
        INSERT INTO usuarios (empresa_id, nome, login, senha, is_admin)
        VALUES (?, ?, ?, ?, ?)
    """, (empresa, nome, login, hashed_password, is_admin))

    conn.commit()
    conn.close()

@eel.expose
def fazer_login(login, senha):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM usuarios WHERE login = ?
    """, (login,))
    resultado = cursor.fetchone()
    conn.close()
    
    if resultado:
        
        hashed_password = resultado[3]
        
        if(check_password(hashed_password, senha)): 
            eel.receber_login(resultado[2], resultado[4])
        else:
            eel.mensagem_usuario("As credenciais informadas estão incorretas.") 
    else:
        eel.mensagem_usuario("As credenciais informadas estão incorretas.") 

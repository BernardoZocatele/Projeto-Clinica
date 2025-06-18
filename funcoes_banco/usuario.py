import sqlite3
import eel
from .gerar_banco import conectar
from criptografia.hashe import hash_password, check_password

@eel.expose
def cadastrar_usuario(nome, login, senha, empresa):
    conn = conectar()
    cursor = conn.cursor()
    
    hashed_password = hash_password(senha)

    cursor.execute("""
        INSERT INTO usuarios (empresa_id, nome, login, senha)
        VALUES (?, ?, ?, ?)
    """, (empresa, nome, login, hashed_password))

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
    
    hashed_password = resultado[3]
    
    if resultado:
        if(check_password(hashed_password, senha)): 
            eel.receber_login(resultado[2])
        else:
            eel.receber_login(None)
    else:
        eel.receber_login(None)

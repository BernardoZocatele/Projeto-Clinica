import sqlite3
import eel

def conectar():
    conn = sqlite3.connect("estoque.db")
    return conn

@eel.expose
def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS empresas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL UNIQUE,
                        endereco TEXT,
                        telefone TEXT,
                        email TEXT,
                        login_admin TEXT NOT NULL,
                        senha_admin TEXT NOT NULL
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        login TEXT NOT NULL,
                        senha TEXT NOT NULL,
                        empresa_id INTEGER NOT NULL,
                        FOREIGN KEY (empresa_id) REFERENCES empresas(id)
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS estoque (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        quantidade INTEGER NOT NULL,
                        minimo INTEGER NOT NULL,
                        empresa_id INTEGER NOT NULL,
                        FOREIGN KEY (empresa_id) REFERENCES empresas(id)
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS logs_estoque (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        usuario TEXT NOT NULL,
                        item TEXT NOT NULL,
                        quantidade INTEGER NOT NULL,
                        acao TEXT NOT NULL,
                        data_hora TEXT NOT NULL,
                        empresa_id INTEGER NOT NULL,
                        FOREIGN KEY (empresa_id) REFERENCES empresas(id)
                    )''')

    conn.commit()
    conn.close()

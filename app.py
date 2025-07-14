import eel 
import funcoes_banco.gerar_banco
import funcoes_banco.usuario
import funcoes_banco.estoque
import funcoes_banco.logs
import os
import sys

def caminho_recurso(relativo):
    if getattr(sys, 'frozen', False): 
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relativo)

db_path = caminho_recurso("estoque.db")
web_path = caminho_recurso("web/index.html")
    

eel.init('web') # Diz para o eel qual o nome da psta que irá conter os arquivos web (html, css, java)
eel.start('login.html') # Inicia o projeto com o nome do arquivo html principal. O arquivo index.html deve estar na pasta web

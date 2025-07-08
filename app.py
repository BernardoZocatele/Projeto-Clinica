import eel # importando biblioteca eel
import funcoes_banco.gerar_banco
import funcoes_banco.usuario
import funcoes_banco.estoque
import funcoes_banco.logs
    

eel.init('web') # Diz para o eel qual o nome da psta que irá conter os arquivos web (html, css, java)
eel.start('login.html') # Inicia o projeto com o nome do arquivo html principal. O arquivo index.html deve estar na pasta web

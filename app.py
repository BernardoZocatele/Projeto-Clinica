import eel # importando biblioteca eel

@eel.expose
def somarNumero(a, b):
    soma = int(a) + int(b)
    
    eel.printarResultados(soma)
    


eel.init('web') # Diz para o eel qual o nome da psta que irá conter os arquivos web (html, css, java)
eel.start('main.html') # Inicia o projeto com o nome do arquivo html principal. O arquivo index.html deve estar na pasta web

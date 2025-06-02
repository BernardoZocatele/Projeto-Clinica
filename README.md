Depois de clonar o repositório (lembre de baixar o git bash):

    Executar o seguinte comando no terminal (PowerSheel) toda vez que for abrir o arquivo:
        .\venv\Scripts\activate

        obs: Você deve estar na pasta de origem do projeto.
    
    Depois de entrar no ambiente virtual:
        Executar o seguinte comando para instalar as bibliotecas utilizadas no projeto:
            pip install -r requirements.txt
    
    Ao finalizar alguma parte do projeto:
        Executar o seguinte comando para atualizar o arquivo requirements.txt:
            pip freeze > requirements.txt


OBS: Sempre entre no ambiente virtual, dessa forma as bibliotecas instaladas não ficarão perdidas na máquina.

from helpers.mensagens.saudacao import boas_vindas
from dados.usuarios.perfil.nome import pegar_nome
from dados.usuarios.conta.email import pegar_email #import absoluto – padrão ideal

if __name__ == "__main__":
    nome = pegar_nome()
    email = pegar_email()

    print(boas_vindas(nome))
    print(f"Email cadastrado: {email}")

"""
Rodar com ---> 
cd sistema
python main.py
"""


##__name__ == "__main__"
#roda o arquivo direto, evita que o código principal rode sem querer ao importar
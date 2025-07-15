from dados.usuarios.perfil.nome import pegar_nome
from dados.usuarios.conta.email import pegar_email

def boas_vindas(nome):
    print(f"Boas vindas {nome}")
    
nome = pegar_nome()
print(nome, pegar_email())

"""
Rodar -->
cd sistema
python -m helpers.mensagens.saudacao

"""
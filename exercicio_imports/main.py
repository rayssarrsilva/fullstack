from helpers.saudacao import ola
from dados.usuario import pegar_usuario

usuario = pegar_usuario()
print(ola(usuario))

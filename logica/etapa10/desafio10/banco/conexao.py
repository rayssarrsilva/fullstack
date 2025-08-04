# Cria conexão com SQLite

import sqlite3 #módulo sqlite3 embutido no Python
import os 

base_dir = os.path.dirname(os.path.abspath(__file__)) #base do arquivo atual
caminho_banco = os.path.join(base_dir, '..', 'data', 'banco.db') #volta um nivel de pasta, acessa a pata data e depois o arquivo

dados = sqlite3.connect(caminho_banco)
cursor = dados.cursor()

def rodar_script(): #sempre que for rodado deleta as tabelas antigas e cria novas
    with open(os.path.join(base_dir, 'script.sql'), mode='r') as script:
        cursor.executescript(script.read())

    dados.commit() #Confirma e grava no disco a última vez que deu commit.
    dados.close() #Fecha a conexão com o banco de dados.

def conectar():
    base_dir = os.path.dirname(os.path.abspath(__file__)) #se posiciona no arquivo atual
    caminho_banco = os.path.join(base_dir, '..', 'data', 'banco.db') #leva ao banco de dados
    
    return sqlite3.connect(caminho_banco) #conecta no caminho do banco de dados

# Armazena as Funções externas, sem classe, responsáveis por salvar e carregar tarefas

from classes.tarefa import Tarefa 
import json
from typing import List
import os 
import csv 
import logging

logging.basicConfig(level=logging.INFO) ## Configure logging
Tarefas = List[Tarefa] #type alias

def salvar_em_json(lista_tarefas: Tarefas, nome_arquivo: str):
    try: 
        lista_serializada = [tarefa.to_dict() for tarefa in lista_tarefas] #O método json.dump não pode serializar diretamente objetos de uma classe personalizada
        #Serializa os objetos da lista usando o método to_dict()

        with open(nome_arquivo, "w", encoding="utf-8") as arquivo: #flag A: adiciona os dados ao final do arquivo existente.

            json.dump(lista_serializada, arquivo, indent=4)

        logging.info(f"Lista salva com sucesso no arquivo {nome_arquivo}")

    except TypeError as e: #Lida com dados que não podem ser convertidos para JSON
        logging.error(f"Erro: Tipo de dado invalido para serialização em JSON. Detalhes: {e}")
        return []
   
    except Exception as e: #Captura qualquer outro erro inesperado
        logging.error(f"Erro inesperado {e}")
        return [] #pra evitar None

    except PermissionError as e:
        logging.error(f"Erro de permissao ao tentar criar o arquivo {nome_arquivo}. Detalhes: {e}")
        return []


def carregar_de_json(nome_arquivo: str) -> Tarefas: #recebe o nome do arquivo e retorna a lista do tipo objetos da classe Tarefas
    
    lista = []
    try: 
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo: #explicitar encoding para evitar problemas em outros SOs
            dados = json.load(arquivo) #decodifica os dados em json pro formato raiz
            for tarefa in dados:
                lista.append(Tarefa.from_dict(tarefa))
        
        return lista 
    
    except FileExistsError:
        logging.error(f"Erro: o arquivo {nome_arquivo} não foi encontrado")
        return lista
    except json.JSONDecodeError:
        logging.error(f"Erro: o arquivo {nome_arquivo} não contem JSON válido")
        return lista #pra evitar None


def salvar_em_csv(lista_tarefas: Tarefas, nome_arquivo: str):

    # cria uma constante pra facilitar manutenção 
    HEADER = ['titulo', 'descricao', 'prioridade', 'status']
    try:
        with open(nome_arquivo, "a", newline='', encoding="utf-8") as arquivo_csv:

            #Cria um objeto que permite escrever no arquivo CSV
            escrever = csv.writer(arquivo_csv) 

            #verifica se o arquivo está vazio
            if os.stat(nome_arquivo).st_size == 0: 
                #Cabeçalho
                escrever.writerow(HEADER)

            #Dados do cabeçalho
            for tarefa in lista_tarefas:
                escrever.writerow([tarefa.titulo, tarefa.descricao, tarefa.prioridade, tarefa.status])

    except FileNotFoundError:
        logging.error(f"O arquivo {nome_arquivo} não foi encontrado")
        return []

    except Exception as e:
        logging.error(f"Ocorreu um erro inesperado: {e}")
        return [] #pra evitar None


def carregar_de_csv(nome_arquivo: str) -> Tarefas:
    """lê um arquivo CSV e retorna uma lista de objetos do tipo Tarefa"""

    lista = []

    try:
        with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo) #mapeia cada linha do arquivo CSV em um dicionário, onde as chaves são os nomes das colunas
            
            for tarefa in leitor:
                linha = Tarefa.from_dict(tarefa) #Para cada linha, cria uma instância de Tarefa usando o método from_dict e adiciona à lista.
                lista.append(linha)

    except FileNotFoundError:
        logging.error(f"O arquivo {nome_arquivo} não foi encontrado")
        return lista
    
    except Exception as e:
        logging.error(f"Ocorreu um erro inesperado: {e}")
        return lista #Evita que o main.py tente iterar sobre None

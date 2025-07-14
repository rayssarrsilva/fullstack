#1. Fundamentos de I/O

# Entrada de dados com input
nome = input("Digite seu nome: ")  # Entrada

# Saída com print formatado
print(f"Olá, {nome.title()}!")  # Saída

#-------------------------------------------------------

#2. Leitura e Escrita de Arquivos .txt


# Escrita em arquivo txt
with open("arquivo.txt", "w") as arq:
    arq.write("Ola, isso e um teste.")

# Leitura de arquivo txt
with open("arquivo.txt", "r") as arq:
    conteudo = arq.read()
    print(conteudo)

#-------------------------------------------------------

#3. Manipulação de Arquivos .json

import json

# Dado em dicionário
dados = {"nome": "Rayssa", "idade": 20}

# Salvar como JSON
with open("dados.json", "w") as f:
    json.dump(dados, f) #objeto a ser serializado e arquivo json onde ele será passado

# Ler JSON e converter de volta pra dict
with open("dados.json", "r") as f:
    info = json.load(f) #decodifica os dados json para o formato objeto em python
    print(info["nome"])

#-------------------------------------------------------

#4. Manipulação de Arquivos .csv

import csv #Comma Separated Values (Cada linha do arquivo representa uma linha da tabela, e cada célula é separada por vírgulas)

# Escrever CSV
with open("dados.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["nome", "idade"])
    writer.writerow(["Rayssa", 20])

# Ler CSV
with open("dados.csv", "r") as f:
    reader = csv.reader(f)
    for linha in reader:
        print(linha)

#-------------------------------------------------------

# 5. Entrada/Saída com Objetos

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def to_dict(self):
        return {"nome": self.nome, "idade": self.idade}

p1 = Pessoa("Rayssa", 20)

# Salvar o objeto como json
with open("pessoa.json", "w") as f:
    json.dump(p1.to_dict(), f)

# Ler e recriar objeto
with open("pessoa.json", "r") as f:
    dados = json.load(f)
    nova_pessoa = Pessoa(**dados)
    print(nova_pessoa.nome)

#-------------------------------------------------------

#  6. Tratamento de Erros com Arquivos

try:
    with open("inexistente.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Arquivo não encontrado!")

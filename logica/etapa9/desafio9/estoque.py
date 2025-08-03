# Funções de controle de fluxo e orquestração

"""
Funções de controle de fluxo:
escolhe o que fazer com base na entrada ou executa uma tarefa repetida

Funções de orquestração:
chamam outras funções em ordem, controlam o fluxo entre diferentes partes do sistema
"""

import csv

#Lista todos os produtos do estoque
def listar_produtos_estoque():
    with open('estoque.csv', mode='r', newline='', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            print(linha)

#Filtrar produtos por categoria
def filtrar_categoria():
    with open('estoque.csv', mode='r', newline='', encoding='utf-8') as categorias:
        ler = csv.DictReader(categorias)

        lista_categoria = [linha['categoria'] for linha in ler if linha['categoria']]

    print(f"As categorias atuais são {set(lista_categoria)}")

    while True: 

        categoria = input("Qual categoria você deseja filtrar (quit/sair/parar)? ").capitalize()

        if categoria in ("Sair", "Parar", "Quit"):
            print("Encerrando filtro de categorias...")
            break
        else:
            with open('estoque.csv', mode='r', newline='', encoding='utf-8') as arquivo:
                leitor = csv.DictReader(arquivo)

                filtro = [linha for linha in leitor if linha['categoria'] == categoria]

                print(f'Os produtos da categoria {categoria} são --> ')
                for produto in filtro:
                    print(f" {produto['nome']} - {produto['preco']} - {produto['quantidade']} ")

#Listar produtos com estoque abaixo de 5 unidades
def estoque_baixo():
    with open('estoque.csv', mode='r', newline='', encoding='utf-8') as arquivo:
        ler = csv.DictReader(arquivo)

        estoque_baixo = [produto for produto in ler if int(produto['quantidade']) < 5]
        print("MOSTRANDO OS PRODUTOS COM ESTOQUE BAIXO: ")

        for produto in estoque_baixo:
            print(f"{produto['nome']} - {produto['quantidade']}")

def listar_filtrar_estoqueBaixo(): #lista produtos, filtra por categoria e mostra os produtos com estoque a baixo de 5 itens
    """
    Função de orquestração
    """
    print("LISTA DE PRODUTOS NO ESTOQUE")
    listar_produtos_estoque()

    filtrar_categoria()
    estoque_baixo()

listar_produtos_estoque()
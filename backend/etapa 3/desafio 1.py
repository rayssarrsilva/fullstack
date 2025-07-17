# Sistema: Gerador de Relatórios de Estudos

"""
Requisitos:
Criar uma função entrada_usuario() que peça o nome e retorne formatado (title())

Criar uma função coletar_estudos(dias) que:

Peça para cada dia:

O nome do dia

A atividade realizada

As horas estudadas

Armazene os dados em uma lista de tuplas ou listas

Retorne a lista

Criar uma função calcular_total_horas(lista) que receba os dados coletados e retorne o total de horas

Criar uma função exibir_relatorio(nome, dados, total_horas) que imprima:

python-repl
Copiar
Editar
Relatório de Estudos - Rayssa
Segunda - Python - 3h
Terça - Git - 2h
...
Total: 12h de estudo

"""

# sem variaveis globais - isolamento entre funções - profissionalismo
# modularização do código todo
# uso de tuplas + nomes verbais nas funções


def nomear_usuario(): #padrao de nomeação verbal
    nome = str(input("Digite seu nome: ")).title()
    return nome


def gerar_relatorio(): #retorna uma lista com os dados principais em tuplas separadas
    
    lista_tupla = [] #evita quebra de isolamento das funções ao usar variavel interna/escopo

    dias = int(input("Quantos dias de estudo deseja registrar? "))

    for dia in range(dias):
        print(f"---Dia {dia+1}---")
        dia_semana = str(input("Dia da semana: ")).lower()

        atividade = str(input("Atividade: ")).title()

        horas_estudadas = int(input("Horas estudadas: "))

        tupla = (dia_semana, atividade, horas_estudadas)
        lista_tupla.append(tupla)

    return lista_tupla #faz salvar os dados na variavel gerar_relatorio()


def calcular_total(parametro): #usa o parametro externo com formato de lista de tuplas (gerar_relatorio())
    total = 0
    for _, _, horas in parametro:
        total = total + horas
    
    return total


def exibir_relatorio():
    nome = nomear_usuario()
    dados = gerar_relatorio()
    total_horas = calcular_total(dados)
    
    print(f"Relatorio de estudos - {nome}")
    for dia, atividade, horas in dados:
        print(f" {dia} - {atividade} - {horas}h")
    print(f"E o total de horas feitas foi {total_horas}")

exibir_relatorio()
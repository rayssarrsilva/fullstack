from entrada_transacao import *
from typing import List, Dict

# from pasta.arquivo import função

"""Modularização
Uso de __all__ para controle de importação
get() no dicionário de categorias
"""


def calcular_total_entradas(lista_dicionario: List[Dict[str, str|float]]) -> float:
    total = 0
    for chave in lista_dicionario:
        if chave["tipo"] == "entrada":
            total = total + chave["valor"]
    return total 

def calcular_total_saidas(lista_dicionario) -> float:
    total = 0
    for chave in lista_dicionario:
        if chave["tipo"] == "saida":
            total = total + chave["valor"]
    return total

def calcular_saldo(lista_dicionario: List[Dict[str, str|float]]) -> float:
    entrada = 0
    saida = 0
    saldo = 0
    for indice in lista_dicionario:
        if indice["tipo"] == "saida":
            saida = saida + indice["valor"]
        else:
            entrada = entrada + indice["valor"]
    saldo = entrada - saida
    return saldo 

def calcular_gastos_categorizados(lista_dicionario: List[Dict[str, str|float]]) -> Dict[str, float]: #retorna um dicionario com chave str e valor float
    dicionario = {}

    for item in lista_dicionario:
        if item["tipo"] == "saida":
            categoria = item["categoria"]
            valor = item["valor"]

            dicionario[categoria] = dicionario.get(categoria, 0) + valor
    return dicionario 

def mostrar_relatorio_final() -> None: #não retorna nada, apenas imprime
    dados = coletar_dados_transacoes() 
    entrada = calcular_total_entradas(dados)
    saida = calcular_total_saidas(dados)
    saldo = calcular_saldo(dados)
    gastos = calcular_gastos_categorizados(dados)

    print("--- RELATÓRIO FINAL ---")

    print(f"Total de entradas: R${entrada}")
    print(f"Total de saídas: {saida}")
    print(f"Saldo Atual: {saldo}")

    print("Gastos por categoria")

    for chave, valor in gastos.items():
        print(f"- {chave}: R$ {valor}")

__all__ = [
    "calcular_total_entradas",
    "calcular_total_saidas",
    "calcular_saldo",
    "calcular_gastos_categorizados",
    "mostrar_relatorio_final"
]



"""
Desafio 2 - Sistema de Análise de Exames Médicos
🎯 Objetivo
Simular um sistema que processa e analisa dados de exames laboratoriais com base em listas paralelas, retornando estatísticas e alertas clínicos.

"""
from typing import List

print("Analise de dados dos Exames laboratoriais")

def entrada() -> tuple[List[str], List[float], List[float], List[int]]:
    """
    Salva a entrada de dados contendo nome, glicose, colesterol e idade de cada respectivo paciente

    Returns:
        tuple[List[str], List[float], List[float], List[int]]: Retorna uma tupla com a lista de nomes, glicose, colesterol e idade de todos os pacientes anotados
    """
    nomes = []
    glicose = []
    colesterol = []
    idade = []

    pacientes = int(input("Quantos pacientes serão analisados? "))

    for paciente in range(pacientes):
        nome = str(input(f"Qual o nome do paciente {paciente+1}: "))
        nomes.append(nome)

        glic = float(input("Qual o nivel de glicose? (mg/dl): "))
        glicose.append(glic)

        col = float(input("Qual o nivel de colesterol total? (mg/dl): "))
        colesterol.append(col)

        idad = int(input("Qual a idade do paciente? "))
        idade.append(idad)

    return nomes, glicose, colesterol, idade 


def glicose_alta(glicose: List[float]) -> int: 
    """
    Conta quantos pacientes estão com glicose acima de 99

    Args: 
        glicose (List[float]): lista do tipo float com o valor da glicose de cada paciente

    Returns:
        int: Retorna a quantidade de pacientes com a glicose acima de 99
    """
    cont = 0
    for glic in glicose:
        if glic > 99:
            cont = cont + 1
    return cont 


def colesterol_acima(colesterol: List[float]) -> int: 
    """
    Conta quantos pacientes estão com colesterol acima de 200

    Args:
        colesterol (List[float]): recebe a lista do tipo float que armazenam os valores de glicose
    
    Returns: 
        int: retorna a quantidade de pacientes com colesterol acima de 200
    """
    cont2 = 0
    for colest in colesterol:
        if colest > 200:
            cont2 = cont2 + 1
    return cont2 


def nome_paciente(nomes: list[str], glicose: List[float]) -> tuple[str, float]: 
    """
    Mostra o nome do paciente com maior índice de glicose

    Args:
        nomes, glicose (List[str], List[float]): recebe a lista de nomes do tipo str, e a lista de glicose do tipo float
    
    Returns: 
        str e float: retorna o nome e a glicose od paciente com o maior indice de glicose
    """
    valor_maximo = max(glicose) #boas práticas
    for nome, glic in zip(nomes, glicose):
        if glic == valor_maximo:
            return nome, glic

#Mostra a média de glicose e colesterol por idade (dividir em faixas etárias: abaixo de 40, 40–60 e acima de 60)
def medir(glicose: List[float], colesterol: List[float], idade: List[int]) -> tuple[float, float, float, float, float, float]: 
    """
    Mostra a média de glicose e colesterol por idade (dividir em faixas etárias: abaixo de 40, 40-60 e acima de 60)

    Args:
        glicose, colesterol, idade (List[float], List[float], List[str]): pega a lista de glicose, colesterol e idade que armazenam os dados de todos os pacientes
    
    Returns:
        tuple[float, float, float, float, float, float]: retorna a média de glicose e colesterol de cada respectiva faixa, se não houver retorna zero.
    """
    dados = list(zip(glicose, colesterol, idade)) 

    dicionario = {
        "abaixo_40": {"glicose": [], "colesterol": []},
        "40-60": {"glicose": [], "colesterol": []},
        "acima_60": {"glicose": [], "colesterol": []}
    }

    #itera sobre dados e cria a variavel temporaria faixa pra usar como key do dicionario, de acordo com a idade do paciente
    for glico, colest, idade in dados: 
        if idade < 40:
            faixa = "abaixo_40"
        elif idade > 60:
            faixa = "acima_60"
        else:
            faixa = "40-60"

        #A cada iteração armazena em uma faixa diferente a glicose + colesterol
        dicionario[faixa]["glicose"].append(glico) 
        dicionario[faixa]["colesterol"].append(colest)

    #inicializa como zero a variavel temporaria e a de armazenamento, pra caso não sejam usadas não de erro no print
    media_colesterol_40 = media_glicose_40 = 0 
    media_colesterol_meio = media_glicose_meio = 0
    media_colesterol_60 = media_glicose_60 = 0
    
    for faixa, tipo in dicionario.items():
        if tipo["glicose"]: #verifica se não está vazio
            media_glicose = sum(tipo["glicose"])/len(tipo["glicose"])
        else:
            media_glicose = 0
        
        if tipo["colesterol"]: #verifica se a lista não está vazia
            media_colesterol = sum(tipo["colesterol"])/len(tipo["colesterol"])
        else:
            media_colesterol = 0
        
        # se a faixa da iteração atual, for igual a respectiva faixa do if, elif ou else, armazena dentro das variaveis corretas a media que acabou de ser feita nas variaveis temporarias.
        if faixa == "abaixo_40":
            media_glicose_40 = media_glicose
            media_colesterol_40 = media_colesterol
        elif faixa == "acima_60":
            media_glicose_60 = media_glicose
            media_colesterol_60 = media_colesterol
        else:
            media_glicose_meio = media_glicose
            media_colesterol_meio = media_colesterol
    
    print(f"Média glicose (<40): {media_glicose_40}, colesterol: {media_colesterol_40}")
    print(f"Média glicose (40-60): {media_glicose_meio}, colesterol: {media_colesterol_meio}")
    print(f"Média glicose (>60): {media_glicose_60}, colesterol: {media_colesterol_60}")

    return media_glicose_40, media_colesterol_40, media_glicose_60, media_colesterol_60, media_glicose_meio, media_colesterol_meio


def acompanhamento(nomes: List[str], glicose: List[float], colesterol: List[float]) -> List[str]:
    """
    Mostra uma lista com nomes dos pacientes que precisam de acompanhamento (glicose > 99 ou colesterol > 200).

    Args:
        nomes, glicose, colesterol (List[str], List[float], List[float]): recebe a lista de nomes, glicose e colesterol
    
    Returns:
        List[str]: retorna a lista de nomes que precisam de acompanhamento

    """

    dados = list(zip(nomes, glicose, colesterol))
    lista_nomes = [] 

    for n, glico, coleste in dados:
        if glico > 99 or coleste > 200:
            lista_nomes.append(n)

    return lista_nomes

def resumo_clinico(nomes: List[str], glicose: List[float], colesterol: List[float], idade: List[int]) -> None:
    """
    Mostra o nome completo, idade, nivel de glicose, nivel de colesterol, status de glicose, status de colesterol e se é recomendado acompanhamento médico para cada paciente

    Args:
        nomes, glicose, colesterol, idade (List[str], List[float], List[Float], List[int]): recebe a lista de nomes, glicose, colesterol e idade que armazena o dado de todos pacientes

    """

    dados = list(zip(nomes, glicose, colesterol, idade))

    for indic, (n, g, c, i) in enumerate(dados):
        print(f"paciente {indic} - {n} tem {i}")
        if g <= 99 and c <= 200:
            print(f"Nivel de glicose atual: {g} - Nivel de colesterol atual: {c} - Niveis normais")
        elif g <= 99 and c > 200:
            print(f"ATENÇÃO: {c} alterado. Nivel de glicose atual: {g}")
            print("Acompanhamento médico sugerido")
        elif g > 99 and c <= 200:
            print(f"ATENÇÃO: {g} alterada. Nivel de colesterol atual: {c}")
            print("Acompanhamento médico sugerido")
        else:
            print(f"ATENÇÃO: Glicose e colesterol alterados. Nivel de glicose: {g} - Nivel de colesterol {c}")
            print("Acompanhamento médico sugerido")
            

__all__ = ["entrada", "glicose_alta", "colesterol_acima", "nome_paciente", "medir", "acompanhamento", "resumo_clinico"]
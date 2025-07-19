"""
Desafio 2 - Sistema de Análise de Exames Médicos
🎯 Objetivo
Simular um sistema que processa e analisa dados de exames laboratoriais com base em listas paralelas, retornando estatísticas e alertas clínicos.

"""

print("Analise de dados dos Exames laboratoriais")

def entrada():
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

# Desempacotando as listas
nomes, glicose, colesterol, idade = entrada()

#Conta quantos pacientes estão com glicose acima de 99
def glicose_alta(glicose): 
    cont = 0
    for glic in glicose:
        if glic > 99:
            cont = cont + 1
    return cont 

#Conta quantos estão com colesterol acima de 200
def colesterol_acima(colesterol): 
    cont2 = 0
    for colest in colesterol:
        if colest > 200:
            cont2 = cont2 + 1
    return cont2 

#Mostra o nome do paciente com maior índice de glicose
def nome_paciente(nomes, glicose): 
    for nome, glic in zip(nomes, glicose):
        if glic == max(glicose):
            return nome 

#Mostra a média de glicose e colesterol por idade (dividir em faixas etárias: abaixo de 40, 40–60 e acima de 60)
def medir(glicose, colesterol, idade): 
    dados = list(zip(glicose, colesterol, idade)) # retorna uma lista com colchetes interno [()]

    dicionario = {
        "abaixo_40": {"glicose": [], "colesterol": []},
        "40-60": {"glicose": [], "colesterol": []},
        "acima_60": {"glicose": [], "colesterol": []}
    }

    #armazena todos os valores nas suas respectivas faixas
    #ao finalizar o bloco de condicionais adiciona os valores no dicionario conforme a faixa
    for glico, colest, idade in dados: 
        if idade < 40:
            faixa = "abaixo_40"
        elif idade > 60:
            faixa = "acima_60"
        else:
            faixa = "40-60"

        dicionario[faixa]["glicose"].append(glico)
        dicionario[faixa]["colesterol"].append(colest)

    
    for idade, tipo in dicionario.items():

        if idade == "abaixo_40":
            faixa = "abaixo_40"
            media_glicose_40 = sum(tipo["glicose"])/len(tipo["glicose"])
            media_colesterol_40 = sum(tipo["colesterol"])/len(tipo["colesterol"])
        elif idade == "acima_60":
            faixa = "acima_60"
            media_glicose_60 = sum(tipo["glicose"])/len(tipo["glicose"])
            media_colesterol_60 = sum(tipo["colesterol"])/len(tipo["colesterol"])
        else:
            faixa = "40-60"
            media_glicose_meio = sum(tipo["glicose"])/len(tipo["glicose"])
            media_colesterol_meio = sum(tipo["colesterol"])/len(tipo["colesterol"])
    
    print(f"Média glicose (<40): {media_glicose_40}, colesterol: {media_colesterol_40}")
    print(f"Média glicose (40-60): {media_glicose_meio}, colesterol: {media_colesterol_meio}")
    print(f"Média glicose (>60): {media_glicose_60}, colesterol: {media_colesterol_60}")

    return media_glicose_40, media_colesterol_40, media_glicose_60, media_colesterol_60, media_glicose_meio, media_colesterol_meio

 #Mostra uma lista com nomes dos pacientes que precisam de acompanhamento (glicose > 99 ou colesterol > 200).
def acompanhamento(nomes, glicose, colesterol):
    dados = list(zip(nomes, glicose, colesterol))
    lista_nomes = [] 

    for n, glico, coleste in dados:
        if glico > 99 or coleste > 200:
            lista_nomes.append(n)

    return lista_nomes

def resumo_clinico(nomes, glicose, colesterol, idade):
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


# armazena toda a lógica computacional sem print, incluindo cálculos e organização

#sintaxe get: dicionario.get(chave, valor_padrao)
#sintaxe sorted: sorted(iterable, key=None, reverse=False)

from typing import Dict, List, Union
from entrada import entrada_chamados_tecnicos

PESO_ABERTO = 2
PESO_RESPOSTA = 1
PRIORIDADE_CONVERSAO = {"baixa": 1, "media": 2, "alta": 3}

def calcular_score(chamado: Dict[str, List[ Union[str, float]]]) -> List[float]:

    lista_scores = []

    for indice in range(len(chamado["titulo"])):
        score = (chamado["tempo_resposta"][indice] * PESO_RESPOSTA) + (chamado["tempo_aberto"][indice] * PESO_ABERTO) + PRIORIDADE_CONVERSAO.get(chamado["prioridade"][indice], 0)
        lista_scores.append(score)

    return lista_scores

chamado = entrada_chamados_tecnicos()
lista_score = calcular_score(chamado)

def atribuir_scores(lista_scores: List[float], chamado: Dict[str, List[ Union[str, float]]]) -> Dict[str, List[ Union[str, float]]]:
    dicionario_scores = {"score": lista_scores}
    chamado.update(dicionario_scores)

    return chamado

chamado_score = atribuir_scores(lista_score, chamado)

def ordenar_chamados(chamado_score: Dict[str, List[ Union[str, float]]]) -> List[Dict[str, Union[str, float]]]:
    """
    Ordenar os chamados pelo maior score ({'titulo': ['bugs', 'requests'], 'prioridade': ['alta', 'media'], 'tempo_resposta': [5.0, 6.0], 'tempo_aberto': [7.0, 5.0], 'setor_responsavel': ['abc', 'z'], 'score': [22.0, 18.0]})
    
    Args:
        chamado_score Dict[str, List[ Union[str, float]]]: recebe o dicionario de listas completo contendo a chave score também
    
    Returns:
        List[Dict[str, Union[str, float]]]: Retorna a lista ordenada com base no maior score pro menor score.
    
    """
    #Une os valores das chaves, combinando os elementos das diferentes listas do dicionario 
    combinados = list(zip(chamado_score["titulo"], chamado_score["prioridade"], chamado_score["tempo_resposta"], chamado_score["tempo_aberto"], chamado_score["setor_responsavel"], chamado_score["score"]))
   
    #List Comprehension: cria o dicionario por meio da iteravel "combiinados"
    novo_dicionario = [

        {"titulo": t,
         "prioridade": p,
         "tempo_resposta": tr,
         "tempo_aberto": ta,
         "setor_responsavel": sr,
         "score": score 
         } 

        for t, p, tr, ta, sr, score in combinados]

    #Ordena a iteravel "novo_dicionario" com a função sorted, e key que usa a chave score do dicionario como critério de ordenação, em ordem Decrescente (maior pro menor)
    ordenado = sorted(novo_dicionario, key= lambda x: x["score"], reverse= True)
    return ordenado 

ordenado = ordenar_chamados(chamado_score)

#Classificar o status com base no score individual de cada chamado.
def classificar_status(ordenado: List[Dict[str, Union[str, float]]]):

    #iterar sobre o dicionario para organizar as condicionais do status
    for chave in ordenado:
        
        score = chave["score"]
        
        if score >= 60:
            status = "critico"
        elif score < 30:
            status = "Normal"
        else:
            status = "Atenção"

        #Se não existe a chave, cria e insere o valor
        chave["status"] = status 

    return ordenado 

print(classificar_status(ordenado))

#Calcular estatísticas com base nos dados dos chamados
def analisar_estatisticas():
    return None

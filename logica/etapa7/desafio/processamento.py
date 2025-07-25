# armazena toda a lógica computacional sem print, incluindo cálculos e organização

#sintaxe get: dicionario.get(chave, valor_padrao)
#sintaxe sorted: sorted(iterable, key=None, reverse=False)

from typing import Dict, List, Union, Optional
from entrada import entrada_chamados_tecnicos

PESO_ABERTO = 2
PESO_RESPOSTA = 1
PRIORIDADE_CONVERSAO = {"baixa": 1, "media": 2, "alta": 3}

def calcular_score(chamado: Dict[str, List[ Union[str, float]]]) -> List[float]:
    """
    Calcula o score de cada chamado

    Args:
        chamado_score Dict[str, List[ Union[str, float]]]: recebe o dicionario de listas completo contendo os dados dos chamados
    Returns:
        List[float]:
    """
    lista_scores = []

    for indice in range(len(chamado["titulo"])):
        score = (chamado["tempo_resposta"][indice] * PESO_RESPOSTA) + (chamado["tempo_aberto"][indice] * PESO_ABERTO) + PRIORIDADE_CONVERSAO.get(chamado["prioridade"][indice], 0)
        lista_scores.append(score)

    return lista_scores

def atribuir_scores(lista_scores: List[float], chamado: Dict[str, List[ Union[str, float]]]) -> Dict[str, List[ Union[str, float]]]:
    dicionario_scores = {"score": lista_scores}
    chamado.update(dicionario_scores)

    return chamado

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

def classificar_status(ordenado: List[Dict[str, Union[str, float]]]) -> List[Dict[str, Union[str, float]]]:
    """
    Classifica o status com base no score individual de cada chamado.
    
    Args:
        ordenado List[Dict[str, Union[str, float]]]: recebe uma lista de dicionarios com chave e valores do tipo str ou float
    Returns:
        List[Dict[str, Union[str, float]]]: retorna uma lista de dicionarios do mesmo tipo do argumento contendo agora o status do chamado (critico, normal ou em atenção)
    """
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


def quantidade_chamados_criticos(ordenado_status: List[Dict[str, Union[str, float]]]) -> int:
    """
    Verifica quantos chamados criticos existem com base nos dados dos chamados
    
    Args: 
        ordenado_status List[Dict[str, Union[str, float]]]: recebe uma lista de dicionarios com a chave em str e os valores em str ou float contendo o status
    Returns:
        int: retorna um numero inteiro que informa a quantidade de chamados criticos foram feitos
    """
    #Quantos chamados são críticos
    criticos_quantidade = 0
    print("---------Quantidade de chamados criticos---------")

    for chave in ordenado_status:
        critico = chave["status"]

        if critico == "critico":
            criticos_quantidade = criticos_quantidade + 1

    if criticos_quantidade == 0:
        print("Não há nenhum chamado critico")
    else:
        print(criticos_quantidade)

    return criticos_quantidade

def chamados_por_setor(ordenado: List[Dict[str, Union[str, float]]]) -> Dict[str, int]:
    """
    Retorna quantos chamados foram feitos por setor

    Args:
        ordenado List[Dict[str, Union[str, float]]]: recebe uma lista de dicionarios com chave e valores do tipo str ou float

    Returns:
        Dict[str, int]: retorna um dicionario com a chave mostrando o nome do setor e a quantidade de chamados feitos
    """
    qtd_chamados = {}

    print("---------Quantidade de chamados por setor---------")

    for chave in ordenado:
        setor = chave["setor_responsavel"]
        if setor:
            qtd_chamados[setor] = qtd_chamados.get(setor, 0) + 1

    for chave, valor in qtd_chamados.items():
        print(f"setor {chave}: {valor}")

    return qtd_chamados

def media_tempo_aberto_criticos(ordenado_status: List[Dict[str, Union[str, float]]]) -> Optional[float]:
    """
    Retorna a média total de tempo aberto de todos os chamados criticos 
    
    Args: 
        ordenado_status List[Dict[str, Union[str, float]]]: recebe uma lista de dicionarios com a chave em str e os valores em str ou float contendo o status
    Returns:
        Optional[float]: retorna a media se a lista não estiver vazia
    """

    print("---------Média de tempo aberto dos chamados críticos---------")
    lista = []

    for c in ordenado_status:
        if c["status"] == "critico":
            lista.append(c["tempo_aberto"])

    if not lista:
        print("ATENÇÃO: Não há chamados criticos")
        return None 
    else:
        media = sum(lista)/len(lista)
        print(media)
        return media 
    


def maior_tempo_aberto(ordenado: List[Dict[str, Union[str, float]]]) -> float:
    """
    Retorna o valor do maior tempo de chamado aberto
    Args:
        ordenado List[Dict[str, Union[str, float]]]: recebe uma lista de dicionarios com chave e valores do tipo str ou float
    Returns:
        float: retorna o maior valor
    """
    
    print("---------Chamado com maior tempo aberto---------")

    lista_tempo = []

    for chave in ordenado:
        lista_tempo.append(chave["tempo_aberto"])

    maior = max(lista_tempo)

    print(maior)
    return maior

def setor_mais_chamados_criticos(ordenado_status: List[Dict[str, Union[str, float]]]) -> Optional[str]:
    """
    Verifica o Setor com mais chamados críticos e retorna o nome desse setor
    Args:
        ordenado_status List[Dict[str, Union[str, float]]]: recebe uma lista de dicionarios com a chave em str e os valores em str ou float contendo o status
    Returns: 
        Optional[str]: retorna o nome do setor com mais chamados criticos caso haja
    """
    print("---------Setor com mais chamados críticos---------")
    chamados_criticos = {} 

    for chamado in ordenado_status:
        if chamado["status"] == "critico" and chamado["setor_responsavel"]:
                nome = chamado["setor_responsavel"]
                chamados_criticos[nome] = chamados_criticos.get(nome, 0) + 1 #adiciona o nome do setor e o valor correspondente de chamados

    if not chamados_criticos:
        print("Não há chamados criticos")
        return None 
    else:
        setor_mais_chamado = max(chamados_criticos, key= chamados_criticos.get)
        print(f"O setor com mais chamados criticos é {setor_mais_chamado} - {chamados_criticos[setor_mais_chamado]} chamados")
        return setor_mais_chamado

def analisar_estatisticas() -> None:
    """
    Junta todas as funções do arquivo e mostra a analise

    Returns:
        None: o que será retornado são as impressoes das proprias funcoes chamadas
    """

    chamado = entrada_chamados_tecnicos() #realiza os inputs e armazena os dados 

    lista_score = calcular_score(chamado) #adiciona o score aos chamados
    chamado_score = atribuir_scores(lista_score, chamado) #ordena o score dos chamados
    ordenado = ordenar_chamados(chamado_score) #ordena os chamados pelo maior score
    ordenado_status = classificar_status(ordenado) #Classifica o status com base no score individual de cada chamado.
    
    quantidade_chamados_criticos(ordenado_status) #Calcular estatísticas com base nos dados dos chamados

    chamados_por_setor(ordenado) #Imprime quantos chamados foram feitos por setor

    media_tempo_aberto_criticos(ordenado_status) #Imprime a média total de tempo aberto de todos os chamados criticos 

    maior_tempo_aberto(ordenado) #imprime o valor do maior tempo de chamado aberto

    setor_mais_chamados_criticos(ordenado_status) #Verifica o Setor com mais chamados críticos e retorna o nome desse setor

    return None 


__all__ = ["calcular_score", "atribuir_scores", "setor_mais_chamados_criticos", "maior_tempo_aberto", "media_tempo_aberto_criticos", "chamados_por_setor", "ordenar_chamados", "classificar_status", "analisar_estatisticas", "quantidade_chamados_criticos",]
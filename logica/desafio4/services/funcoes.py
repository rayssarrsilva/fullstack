from models.tarefa import Tarefa

def filtrar_tarefas_concluidas(lista_tarefas: list): #List[Tarefa] 
    for a in lista_tarefas:
        if a.status == "Concluida":
            print(a) #exibe

    return list(filter(lambda tarefa: tarefa.status == "Concluida", lista_tarefas)) #return: Retorna um valor de uma função, permitindo que resultados da função possam ser usados em outras partes do código.

def contar_por_prioridade(lista_tarefa, prioridade: str):

    filtro_prioridade = list(filter(lambda tarefa: tarefa.prioridade == prioridade, lista_tarefa))
    quantidade = len(filtro_prioridade)

    return quantidade

def obter_titulos(lista_tarefas: list):
    print("Lista de titulos: ")
    titulos = [t.titulo for t in lista_tarefas]

    for titulo in titulos:
        print(titulo)

    return titulos

from functools import reduce 

def contar_tarefas_total(lista_tarefas: list[Tarefa]) -> int: #Argumento do tipo lista de objeto, que retorna um inteiro 

    contador = reduce(lambda contador, _: contador + 1, lista_tarefas, 0)
    print(f"O total de tarefas é {contador}")
    #reduce(funcao, iteravel, valor_inicial_opcional)
    return contador 

#Contador Inteligente de Tarefas
"""Fazer um sistema que recebe tarefas do usuário e imprime uma lista organizada, com controle de fluxo.

🧱 Requisitos:
Perguntar quantas tarefas serão registradas

Usar for com range() para pedir os nomes das tarefas

Armazenar em uma lista

Mostrar todas usando enumerate()

Se a tarefa for "descansar", usar continue (não mostrar o número)

Se for "parar", usar break e encerrar a contagem

Ao final, mostrar quantas tarefas foram realmente listadas com len()

"""

print("Contador inteligente de tarefas")
quantidade = int(input("Quantas tarefas serão registradas? "))

tarefas = [] #lista de tarefas vazias onde serão armazenadas

for _ in range(quantidade):
    name = str(input("Digite o nome de cada tarefa: ")).lower() #deixa minuscula, para filtrar no if do enumerate
    tarefas.append(name)

contador = 0
print("As tarefas armazenadas são: ")
for indice, tarefa in enumerate(tarefas):
    contador += 1
    
    if tarefa == "descansar":
        continue
    else:
        print(f"{indice} - {tarefa}")

print(f"foram listadas {contador} tarefas")
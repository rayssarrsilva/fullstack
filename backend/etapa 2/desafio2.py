#Desafio 2 – Planejador de Semana Personalizado

"""Objetivo:
Simular o planejamento de estudo da semana, usando tudo aprendido.

🧱 Requisitos:
Pedir o nome do usuário

Fazer um for que percorre a lista: ["segunda", "terça", ..., "domingo"]

Em cada dia:

Se dia for sábado → imprimir "descansar"

Se dia for domingo → "revisar"

Senão → "estudar backend"

Se o nome do usuário for "Rayssa" e o dia for quarta, usar and e printar: "Quarta especial de código!"

Após cada dia, perguntar se quer continuar (s ou n)

Se não quiser, usar break

Ao final, usar len() para mostrar quantos dias foram planejados

"""

print("Planejador de Semana Personalizado")
nome = str(input("Digite seu nome: ")).title() #Converte a primeira letra pra maiusculo

print("preparando sua semana...")
LISTA = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabado", "Domingo"]

contador = 0 #Conta os dias que foram planejados

for dia in LISTA:
    contador += 1
    if dia == "Sabado":
        print(f"{dia} - Dia de descansar")
    elif dia == "Domingo":
        print(f"{dia} - dia de revisar")
    elif dia == "Quarta" and nome == "Rayssa":
        print(f"{dia} - especial de código")
    else:
        print(f"{dia} - Dia de Estudar backend")

    continuar = str(input("Deseja continuar? (s/n)"))
    if continuar == "n":
        break
    elif continuar != "s":
        print("Você digitou errado, digite novamente")

print(f"Parabens {nome}, continue focado! você planejou {contador} dias")



"""
Condicionais (if, elif, else), Operadores lógicos (and, or, not), Comparações (==, !=, <, >, etc.), Estruturas de repetição (while, for), Funções auxiliares: range(), len(), enumerate() e Controle de fluxo: break, continue

"""
# Simulador de Rotina Inteligente


"""
Pergunta o nome do usuário - check

Pede o dia da semana - check

Com base no dia, sugere uma atividade:

Segunda a sexta: “Estudar Python”

Sábado: “Descansar um pouco”

Domingo: “Revisar tudo da semana”

Conta regressivamente de 3 a 1 com while - check

Finaliza com uma mensagem de motivação

"""

nome = str(input("Qual o nome do usuário: "))
dia = str(input("Qual o dia da semana? ")).lower() #aceita "Segunda" ou "segunda"

sabado = "Descansar um pouco"
domingo = "Revisar tudo da semana"

print("preparando...")

contador = 0

while contador < 3:
    contador += 1
    print(contador)
print("preparando...")

if dia in ["segunda", "terça", "quarta", "quinta", "sexta"]:
    print("Estudar python")
elif dia == "sabado":
    print(sabado)
elif dia == "domingo":
    print(domingo)
else:
    print("Esse dia da semana não é valido")

print("Continue focado(a) ", nome)
#Relatório Semanal de Hábitos

"""
📋 O que o sistema faz:
Coleta informações sobre os hábitos do usuário durante a semana

Usa lógica condicional e loops para processar a rotina diária

Aplica controle de fluxo para ignorar dias sem hábitos ou parar o processo

Ao final, gera um relatório enumerado com análise dos dias úteis

Faz um cálculo simples de média e imprime a quantidade real de hábitos registrados

"""

print("Olá! Bem-vindo ao seu Relatório Semanal de Hábitos. (para sair do sistema, digite 'cancelar')")
nome = str(input("Digite seu nome: ")).lower()
re_dias = int(input("Quantos dias você deseja registrar? "))

habitos_registrados = 0
lista_dias = []
lista_atividade = []

for dia in range(re_dias):  

    print(f"--- Dia {dia+1} ---")

    dia_semana = str(input("Qual dia da semana? ")).lower()
    lista_dias.append(dia_semana)

    print("Preparando registro...")
    print("3")
    print("2")
    print("1")

    habitos = str(input("Você teve hábitos saudáveis hoje? (sim ou não) "))

    if habitos in ("n", "não", "nao"):
        print("Nenhum hábito registrado. Pulando dia...")
    elif habitos in ("s", "sim"):
        habitos_registsrados += 1

        atividade = str(input("Digite o principal hábito de hoje: "))
        lista_atividade.append(atividade)

        if (dia+1) == re_dias: #O iterador dia, inicia com 0. Se o iterador for igual a quantidade de dias, ele pode parar. Se não, ele continua perguntando se o usuario deseja continuar.
            break
        else:
            continuar = str(input("Deseja continuar?(s/n) "))

        if continuar in ("n", "não", "nao"):
            break
    else:
        print("Você digitou algo errado. Sistema finalizando...")
        break


horas_acumuladas = habitos_registrados * 2

print("Resumo da sua semana")
for index, (lista_dias, lista_atividade) in enumerate(zip(lista_dias, lista_atividade)):
    print(f"{index+1}. {lista_dias} - {lista_atividade}")

print(f"Você registrou hábitos em {habitos_registsrados} dia(s) uteis")
print(f"Se você estudou 2h por dia útil, você acumulou {horas_acumuladas} horas de progresso esta semana")

#Relatório de Atendimento da Clínica
#O sistema precisa calcular a média de espera, o tempo mínimo, o tempo máximo e o número de atendimentos acima de 40 minutos.

minutos = [32, 45, 27, 50, 39, 40, 33]

quantidade = len(minutos)
soma = sum(minutos)
media = soma/quantidade
minimo = min(minutos)
maximo = max(minutos)

contador = 0
for atendimento in minutos:
    if atendimento > 40:
        contador += 1

print(f"A média de espera do paciente é {media:.1f}, o tempo minimo de espera é {minimo}, o máximo é {maximo}, e o número de atendimentos acima de 40 minutos é {contador}")
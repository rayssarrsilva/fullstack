# Mini Projeto: “Calculadora de Rotina”
"""Mostra um menu com 3 operações: somar horas de estudo, multiplicar metas diárias e calcular média de concentração (ex: (nota1 + nota2) / 2)"""

print("Bem vindo ao menu")
print("1 - somar ")
print("2 - multiplicar metas ")
print("3 - calcular média de concentração ")

opcao = int(input("Digite 1, 2 ou 3 -> "))
n1 = float(input("Primeiro número: "))
n2 = float(input("Segundo número: "))

soma = n1 + n2
multiplicação = n1 * n2 
média = (n1 + n2) / 2

print("A soma é", soma ,  " a multiplicação das metas diárias é ", multiplicação, " e a média de concentração é ", média)


"""correção:
- Um \n deixa a saída mais organizada.
- Evite acentos em nomes de variáveis
"""

"""resumo: 
- Operações aritméticas e Operadores aritméticos	
- Tipos primitivos
- Execução linear (sequencial)
- Conversão de tipos	
- Atribuição de variáveis	
"""
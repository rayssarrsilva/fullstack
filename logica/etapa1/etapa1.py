"""Mini Desafios Didáticos"""

#Explique, com suas palavras, a diferença entre for e while e me dê um exemplo da vida real para cada.
"""Resposta: O for serve para iterar sobre uma quantidade especifica de itens (numeros, letras, etc) em uma lista/tupla/dicionario ou qualquer outra variavel de armazenamento.
Já while serve para iterar ate que algo seja verdadeiro ou falso.
"""

#Crie uma função eh_par(numero) que retorna True se for par.
def eh_par(numero):
    if numero % 2 == 0:
        print("True")
    else:
        print("False")
    
#eh_par(5)

#Simule um elevador que só aceita subir com senha correta (usar while).

senha = 0
while senha != 68:
    senha = int(input("Digite a senha: "))
print("Senha correta")

# Crie uma função verificar_idade que retorna se a pessoa é menor, adulta ou idosa.

def verificar_idade(idade):
    if idade >= 18:
        print("voce é maior de idade")
    else:
        print("Voce é menor de idade")

verificar_idade(18)

# Escreva um código que calcule o valor total de uma compra de 3 produtos e diga se o cliente pode parcelar (valor > 100).

total = 0
print("Calculo do total do valor de 3 produtos e se ele pode ser parcelado (valor maior que 100)")

for a in range(3):
    produto = int(input("Qual o valor do produto? "))
    if produto > 100:
        parcelar = input("Você deseja parcelar? (s/n)").lower()
        if parcelar in ("s", "sim"):
            print("produto parcelado")
            
    total = total + produto

print(f"O total da compra dos 3 produtos foi {total}")
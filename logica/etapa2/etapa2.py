# Escreva o pseudocódigo para um programa que calcule o dobro de um número.

"""
Inicio
Ler numero
Criar variavel com o nome dobro
adicionar na variavel dobro o calculo: Numero * 2
Escreva dobro (variavel)
""" 

#Crie um algoritmo que conte quantos números pares existem entre 1 e 50.
def algoritmo():
    contador = 0
    for a in range(1,50):
        if a % 2 == 0:
            contador = contador + 1
        
    print(f"De 1 a 50 possuem {contador} números pares")

# Simule um caixa eletrônico que só entrega notas de 100, 50, 20, 10 e 2.
def caixa():
    sacar = int(input("Quanto voce deseja sacar? "))
    notas = [100, 50, 20, 10, 2]
    caixa = {}

    sacar = round(sacar / 10) * 10

    for nota in notas:
        
        quantidade = sacar // nota #a cada iteração será feita a divisao do valor que se deseja sacar por um dos valores da lista, mostrando a quantidade de cada pra divisao do saque
        
        if quantidade > 0: #Se a quantidade for maior que zero, continua a salvar na variavel CAIXA
            caixa[nota] = quantidade #Salvar o valor da lista seguido pela quantidade de vzs que ele foi dividido pelo mesmo
            sacar = sacar % nota  #Salva o resto da divisao do valora sacar pelo valor da nota na lista, e na próxima repetição o valor a sacar diminui sendo necessario alterar a nota na variavel quantidade

    for nota, quantidade in caixa.items():
        print(f"{quantidade} de notas de {nota}")

#Dado um vetor de 10 números, calcule a média e diga quais estão acima da média.
import math 

def vetor():
    lista = []
    for a in range(10):
        numero = int(input(f"Digite o numero {a+1}: "))
        lista.append(numero)

    media = sum(lista)/10
    media = math.floor(media)
    contador = 0
    for numero in lista:
        if numero > media:
            contador = contador + 1
    print(f"A média é {media} e posseum {contador} numeros a cima da media")

# Crie um sistema de apuração de votos para 3 candidatos, com total e percentual.

def votacao():
    a = []
    b = []
    c = []
    nulo = []
    for voto in range(1, 11):
        votacao = input("Em quem voce deseja votar? canditados = [ A, B, C e vazio para contabilizar como nulo]: ").upper()
        if votacao in ("A", "B", "C"):
            if votacao == "A":
                a.append(votacao)
            elif votacao == "B":
                b.append(votacao)
            elif votacao == "C":
                c.append(votacao)
        else:
            nulo.append(votacao)

    print(f"O canditado A teve {len(a)} votos o canditado B teve {len(b)} votos e o canditado C teve {len(c)} votos. \n O total de votos nulos foi {len(nulo)}")
    total = a + b + c
    print(f"O percentual de votos do canditado A foi: {round((len(a)/len(total))*100)}% . O de B foi: {round((len(b)/len(total))*100)}% , o de C foi {round((len(c)/len(total))*100)}% e de votos nulos: {round((len(nulo)/len(total))*100)}% ")

caixa()
# 1. Crie uma classe Pessoa com atributos nome e idade, e método falar().
class Pessoa():
    def __init__(self, nome, idade): #função consstrutora
        self.nome = nome.title()
        self.idade = int(idade)
    
    def falar(self):
        print(f"{self.nome} está falando....")
        print(f"OI, tenho {self.idade} anos!")

objeto = Pessoa("rayssa", 19)
objeto.falar()

# 2. Crie uma classe Funcionario que herda de Pessoa, com método bater_ponto().
class Funcionario(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    
    
    def bater_ponto(self):
        print(f"A funcionaria {self.nome} de {self.idade} está batendo o ponto..")

# 3. Faça uma função filtrar_maiores_de_idade(lista) usando filter.
lista = [10, 4, 3, 2, 6, 7, 9, 19, 18, 20]

def filtrar_maiores_de_idade(lista):
    print(list(filter(lambda x: x >= 18, lista))) #Filtra elementos de uma lista com base em uma condição [filtra]

filtrar_maiores_de_idade(lista)

# 4. Crie uma função pura soma_quadrados(lista) que retorna a soma dos quadrados dos números.

def soma_quadrados(lista):
    print(list(map(lambda x: x ** 2, lista))) #map: Aplica uma operação a cada elemento de uma lista [aplica]

soma_quadrados(lista)

# 5. Divida um sistema simples de mensagens em dois arquivos: main.py e mensagem.py (simulando modularização).
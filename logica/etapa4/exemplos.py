# Paradigma Imperativo (usado quando o sistema é simples ou script temporário)
funcionarios = []

for _ in range(3):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    cargo = input("Cargo: ")
    funcionarios.append({"nome": nome, "idade": idade, "cargo": cargo})

print("Funcionários autorizados:")
for f in funcionarios:
    if f["idade"] >= 18:
        print(f["nome"])

# Paradigma Funcional (usado para processamento de dados, filtros, manipulação de listas)

def maior_de_idade(funcionario):
    return funcionario["idade"] >= 18

funcionarios = [
    {"nome": "Ana", "idade": 20, "cargo": "Dev"},
    {"nome": "Beto", "idade": 16, "cargo": "Estagiário"}
]

autorizados = list(filter(maior_de_idade, funcionarios))
nomes = list(map(lambda f: f["nome"], autorizados))

print(nomes)


#Paradigma Orientado a Objetos (OOP)
from datetime import datetime

# Classe-base com atributos comuns
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        print(f"Olá, sou {self.nome} e tenho {self.idade} anos.")


class Funcionario(Pessoa): #herança
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade)  # herança + evita duplicação de código
        self.cargo = cargo
        self.pontos = []  # encapsulamento: atributo interno
    
    def bater_ponto(self):
        horario = datetime.now().strftime("%H:%M")
        self.pontos.append(horario)
        print(f"{self.nome} bateu o ponto às {horario}.")
    
    def apresentar(self):  # polimorfismo: redefinido na classe filha
        print(f"{self.nome}, {self.cargo}, idade: {self.idade}")

# Usando modularização (poderia estar em outro arquivo)
def filtrar_maiores(lista_func): #função pura: Ausência de efeitos colaterais
    return [f for f in lista_func if f.idade >= 18]

# Criando instâncias
rayssa = Funcionario("Rayssa", 25, "Backend Developer") #Objeto da classe
joao = Funcionario("João", 17, "Estagiário") #Objeto

funcionarios = [rayssa, joao]

# Chamando métodos
for f in funcionarios:
    f.apresentar()
    f.bater_ponto()

# Filtro com programação funcional
autorizados = filtrar_maiores(funcionarios)

print("\nAcesso liberado para:")
for f in autorizados:
    print(f.nome)


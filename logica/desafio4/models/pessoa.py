class Pessoa():
    def __init__(self, nome, idade): #construtor que define no argumento os atributos obrigatorios pra criar o objeto da classe Pessoa
        self.nome = str(nome).title()
        self.idade = int(idade)
    
    def __str__(self):
        print(f"nome: {self.nome} - idade {self.idade}")
    def falar(self):
        return f"{self.nome} está falando..."

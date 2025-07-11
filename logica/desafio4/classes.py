class Pessoa():
    def __init__(self, nome, idade): #construtor que define no argumento os atributos obrigatorios pra criar o objeto da classe Pessoa
        self.nome = str(nome).title()
        self.idade = int(idade)
    
    def __str__(self):
        print(f"nome: {self.nome} - idade {self.idade}")
    def falar(self):
        return f"{self.nome} está falando..."

class Tarefa():
    def __init__(self, titulo: str, descricao: str, prioridade: str, status: str):
        self.titulo = str(titulo).title()
        self.descricao = str(descricao).lower()
        self.prioridade = str(prioridade).title()
        self.status = str(status).title()

    def __str__(self) -> str: #Define a representação do objeto em formato string (como usamos esse objeto pra ser inserido dentro da lista na classe Funcionario, ele será representado como é mostrado no __str__)
        return f"{self.titulo} - {self.descricao} - {self.prioridade} - {self.status}" #exibir titulo e descricao  do objeto de forma clara

    def resumir(self):
        print(f"Tarefa: {self.titulo}. Descrição: {self.descricao}. Prioridade: ({self.prioridade}). Status atual: {self.status}") #Retorna string com detalhes da tarefa
    
    def concluir(self):
        self.status = "Concluida"
        print(f"A tarefa {self.titulo} foi concluida")

import time #Biblioteca de horas. (Usada pra mostrar o horário que está sendo bátido o ponto do funcionário.)

class Funcionario(Pessoa):
    def __init__(self, nome: str, idade: int, cargo: str):
        super().__init__(nome, idade) #função super() + construtor da classe herdada + respectivos atributos herdados (todos)
        self.cargo = str(cargo).title()
        self.tarefas: list[Tarefa] = [] # type hint (armazena os objetos da classe Tarefa) (boas praticas de nome da lista no plural)

    def bater_ponto(self): 
        #Exibe mensagem com nome e horário de ponto

        tempo_atual = time.localtime()
        hora_formatada = time.strftime("%H:%M", tempo_atual) #Altera o formato da variavel que salva o tempo
        dia_formatado = time.strftime("%d/%m", tempo_atual)
        print(f"O(a) funcionario {self.nome} esta batendo o ponto as {hora_formatada} do dia {dia_formatado}.")

    def atribuir_tarefa(self, tarefa: Tarefa): # (Type Hint) self (permite chamar os atributos definidos) e tarefa do tipo Objeto Tarefa (parametro:tipo)
        if not isinstance(tarefa, Tarefa): 
            raise TypeError("Você precisa inserir a instancia(objeto) da classe tarefa nesse método")
        else:
            self.tarefas.append(tarefa)
            print(f"tarefa {tarefa.titulo} atribuida") #Mostra o atributo titulo do objeto tarefa que foi passado como argumento
    
    def listar_tarefas(self):
        print(f"Tarefas do funcionario: {self.nome}")
        return [t for t in self.tarefas]

    def resumir_tarefa(self):
        print("Preparando o resumo.... ")

        resumo = [tarefa.resumir() for tarefa in self.tarefas]
        return resumo #Evita o none que aparece ao usar print, e retorna todas as tarefas. 
        # variavel que se repete for variavel iteradora in lista pra ser iterada

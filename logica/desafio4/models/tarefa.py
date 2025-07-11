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
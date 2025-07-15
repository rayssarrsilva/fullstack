class Tarefa():
    def __init__(self, titulo: str, descricao: str, prioridade: str, status: str):
        self.titulo = titulo
        self.descricao = titulo 
        self.prioridade = prioridade
        self.status = status #Self faz referencia a própria instancia de uma classe

    def __str__(self) -> str: #Retornara um str
        return self.titulo, self.descricao, self.prioridade, self.status
    
    def resumir(self):
        print(f"Tarefa: {self.titulo}. Descrição: {self.descricao}. Prioridade: ({self.prioridade}). Status atual: {self.status}") 

    def concluir(self):
        self.status = "Concluida"
        print("A tarefa foi concluida")



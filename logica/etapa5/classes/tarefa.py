class Tarefa():    
    def __init__(self, titulo: str, descricao: str, prioridade: str, status: str):
        self.titulo = titulo
        self.descricao = descricao 
        self.prioridade = prioridade
        self.status = status #Self faz referencia a própria instancia de uma classe

    def __str__(self) -> str: # __str__ deve retornar uma string formatada
        return f"{self.titulo} , {self.descricao}, {self.prioridade}, {self.status}"
    
    def resumir(self):
        print(f"Tarefa: {self.titulo}. Descrição: {self.descricao}. Prioridade: {self.prioridade}. Status atual: {self.status}") 

    def to_dict(self): #serializa a tarefa em um dicionario
        return {
            "titulo": self.titulo,
            "descricao": self.descricao,
            "prioridade": self.prioridade,
            "status": self.status
        }
    
    @classmethod 
    def from_dict(cls, dados): #cls, which refers to the class itself e dados refere-se aos dados que serão passados como parametros
        return cls(
            dados["titulo"],
            dados["descricao"], 
            dados["prioridade"], 
            dados["status"])
    # serializa o dicionario em um objeto da propria classe (@classmethod)

class ListaTarefas(): #padrão PEP8 para nomes de classes: PascalCase
    def __init__(self):
        self._lista = [] #lista privada, só pode ser acessada com métodos da classe

    def __str__(self):
        return f"{self._lista}"
    
    def adicionar_tarefa(self, tarefa: Tarefa):
        if not isinstance(tarefa, Tarefa):
            raise TypeError("Você precisa adicionar um objeto da classe Tarefa")
        else:
            self._lista.append(tarefa)
            print(f"Tarefa salva na lista com sucesso")

    def listar(self):
        for a in self._lista:
            print(a)


t1 = Tarefa("Estudar ingles", "Assistir videos em ingles", "Alta", "Fazendo")
dados = t1.to_dict()

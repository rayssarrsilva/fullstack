from classes.tarefa import Tarefa, ListaTarefas
from services.persistencia import *

t1 = Tarefa("Estudar ingles", "Assistir videos em ingles", "Alta", "Fazendo")

tarefas = ListaTarefas()
tarefas.adicionar_tarefa(t1)
tarefas.listar()
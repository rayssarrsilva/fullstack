from models.pessoa import Pessoa
from models.funcionarios import Funcionario
from models.tarefa import Tarefa

from services.funcoes import (
    filtrar_tarefas_concluidas,
    contar_por_prioridade,
    obter_titulos,
    contar_tarefas_total
)



def main():
    p1 = Pessoa("Mariana", 50)

    print(p1.falar())
    print(p1.idade)
    print(p1.nome)

    t1 = Tarefa("Analisar dados", "Desenvolver sistema de tarefas", "media", "concluida")
    t1A = Tarefa("Analisar dados", "Organizar arquivos", "media", "concluida")
    t2 = Tarefa("Analisar financeira", "Analisar dados da planilha financeira", "media", "pendente")
    t3 = Tarefa("Analisar jogos", "Analisar dados da planilha de hoje", "media", "concluida")

    x01 = Funcionario("Rayssa", 19, "Desenvolvedora")

    x01.atribuir_tarefa(t1)
    x01.atribuir_tarefa(t1A)
    x01.atribuir_tarefa(t2)
    x01.atribuir_tarefa(t3)
    x01.falar()
    x01.nome
    x01.bater_ponto()
    x01.listar_tarefas()
    x01.resumir_tarefa()

    tarefas = x01.tarefas #servira de teste pras funcoes que pedem a lista do objeto

    filtrar_tarefas_concluidas(tarefas)
    contar_por_prioridade(tarefas, "Media")
    obter_titulos(tarefas)
    contar_tarefas_total(tarefas)

if __name__ == "__main__":
    main()
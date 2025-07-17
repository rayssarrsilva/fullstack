from classes.tarefa import Tarefa, ListaTarefas
from services.persistencia import salvar_em_json, salvar_em_csv, carregar_de_json, carregar_de_csv
import os 

"""
Lógica esperada:
Exibir menu principal - CHECK input

Usuário escolhe opção:
Criar nova tarefa - CHECK input
Ver todas as tarefas - CHECK input
Salvar em JSON - CHECK input 
Carregar de JSON - CHECK input
Salvar em CSV - CHECK input
Carregar de CSV - CHECK input
Sair - CHECK

Chamar a função correspondente - CHECK
Repetir até o usuário sair - CHECK while

"""

def main():
    print("----- MENU PRINCIPAL ----")

    lista = ListaTarefas()

    def criar_tarefa():
        tarefa = str(input("Digite o titulo da tarefa: ")).strip().lower()
        descricao = str(input("Digite a descricao da tarefa: ")).strip().lower()
        prioridade = str(input("Digite a prioridade da tarefa: ")).strip().lower()
        status = str(input("Digite o status da tarefa: ")).strip().lower()

        return Tarefa(tarefa, descricao, prioridade, status)
    
    while True:
        os.system("cls" if os.name == "nt" else "clear") #retorne o nome do sistema operacional, nt indica que o sistema é Windows, se for usa cls comando windows pra limpar senão usa clear (Unix, Linux e MacOS)
        continuar = str(input("1- adicionar uma tarefa ao relatorio [adicionar]  (Ou digite sair) ")).strip()
        if continuar.lower() == "sair":
            break
        elif continuar.lower() in ("adicionar", "1"):
            tarefa_usuario = criar_tarefa()
            
            lista.adicionar_tarefa(tarefa_usuario)

            listar = str(input("Deseja listar as tarefas salvas na lista? (sim/nao) ")).lower().strip()
            if listar == "sim":
                print("LISTA DE TAREFAS NO RELATORIO ---> ")
                lista.listar()
            
            salvar = str(input("1- Salvar em JSON \n 2- Salvar em CSV \n 3- Continuar adicionando tarefas (digite o numero)")).lower().strip()
            if salvar == "1":
                arquivo_json = input("Digite o nome do arquivo com extensão JSON que deseja salvar: ").strip()
                salvar_em_json(lista.lista, arquivo_json)
            elif salvar == "2":
                arquivo_csv = input("Digite o nome do arquivo com extensão CSV que deseja salvar: ").strip()
                salvar_em_csv(lista.lista, arquivo_csv)            

            carregar = str(input("Deseja carregar algum arquivo JSON ou CSV? se sim, digite a extensão dele (digite não, para continuar)")).strip().lower()
            
            if carregar == "json":
                carregar_json = str(input("Digite o nome do arquivo JSON que você deseja carregar: ")).strip()
                for tarefa in carregar_de_json(carregar_json):
                    print(tarefa)
            
            elif carregar == "csv":
                carregar_csv = str(input("Digite o nome do arquivo CSV que você deseja carregar: ")).strip()
                for tarefa in carregar_de_csv(carregar_csv):
                    print(tarefa)

## This ensures the script runs only when executed directly
if __name__ == "__main__":
    main() 
#This condition checks if the script is being run directly (not imported as a module). If true, it calls the main() function

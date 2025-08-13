from banco.operacoes import *


if __name__ == "__main__":
    print("Insira clientes da locadora na tabela --> ")
    quantidade = int(input("Quantos clientes deseja registrar? "))

    for cliente in range(quantidade):
        nome = input(f"Nome do cliente {cliente+1}: ")
        email = input(f"Email do cliente {cliente+1}: ")
        id = inserir_clientes(nome, email)
        print(f"O seu ID é {id}")

    #adiciona a quantidade de filmes desejada no catalogo
    print("---INSIRA OS FILMES DO CATALOGO---")

    quantidade = int(input("Quantos filmes deseja inserir no catalogo? "))
    for filme in range(quantidade):
        titulo = str(input("Titulo do filme: "))
        categoria = str(input("Qual a categoria do filme? "))
        preco_aluguel = float(input("Digite o preco do aluguel? "))
        id = inserir_filmes(titulo, categoria, preco_aluguel)
        print(f"O ID do filme salvo é {id}")

    #permite o cliente registrado alugar filmes
    quantidade = int(input("Quantos alugueis você deseja fazer? "))
    for aluguel in range(quantidade):
        idcliente = int(input("Digite o id do cliente que efetuara o aluguel: "))
        idfilme = int(input("Digite o id do filme que será alugado: "))
        devolvido = int(input("O filme foi devolvido ou alugado? (0= Devolvido, 1= Alugado) "))
        registrar_aluguel(idcliente, idfilme, devolvido)

    #permite deletar algum cliente pelo id
    quantidade = int(input("Deseja deletar quantos clientes? "))
    for cliente in range(quantidade):
        id_cliente = int(input("Qual o id do cliente que você deseja deletar? "))
        deletar_cliente(id_cliente)

    
    #permite altear o status de devolução na tabela alugados caso o filme seja alugado
    quantidade = int(input("Deseja alterar o status de aluguel quantos filmes? "))
    for cliente in range(quantidade):
        status = int(input("Devolver: 0 ou Não: 1 (digite 0 ou 1)-> "))
        id_aluguel = int(input("Qual o id do aluguel que deseja alterar o status? "))
        atualizar_status_devolucao(status, id_aluguel)

    print("----RELATORIO DA LOCADORA LOCAL----")

    #Mostra o valor total dos filmes alugados por clientes
    lista_tupla = valor_total_filmes_alugados_por_cliente()
    contador = 0
    for _, nome, soma in lista_tupla:
        contador = contador + 1
        print(f"{contador}-cliente: {nome} - R$ {soma}")

    #lista todos os alugueis existentes
    lista_alugueis = listar_alugueis()
    for nome, titulo in lista_alugueis:
        print(f"O(a) cliente {nome} aluguou o filme {titulo}")

    #lista dos clientes que mais alugaram filmes
    print("-----Os clientes que mais alugaram filmes foram----- ")
    lista = listar_top3_clientes()
    if not lista:
        print("ATENÇÃO: a lista está vazia")
    else:
        for cliente in lista:
            print(cliente)

    #lista de filmes alugados e nao devolvidos
    nao_devolvido = alugados_nao_devolvidos()
    print("----Veja a lista de filmes alugados que ainda nao foram devolvidos---- ")
    if not nao_devolvido:
        print("ATENÇÃO: a lista está vazia")
    else:
        for alugados in nao_devolvido:
            print(alugados)
        

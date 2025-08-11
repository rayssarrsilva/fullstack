# Funções que executam INSERT, SELECT, etc
from conexao import conectar 

#Inserir clientes
def inserir_clientes(nome: str, email:str):
     #conecta ao banco de dados
    conecta = conectar()

    #cria o cursor para manipular em SQL o banco de dados
    cur = conecta.cursor()

    cur.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", (nome, email))
    print("Os dados do cliente foram armazenado no banco de dados!")

    conecta.commit()
    conecta.close()

#Inserir filmes 
def inserir_filmes(titulo: str, categoria:str, preco_aluguel:float):
    conecta = conectar()
    cur = conecta.cursor()

    if isinstance(preco_aluguel, str):
        preco_aluguel = preco_aluguel.replace(",",".")
    else:  
        preco_aluguel = float(preco_aluguel)

    cur.execute("INSERT INTO filmes (titulo, categoria, preco_aluguel) VALUES (?, ?, ?)", (titulo, categoria, preco_aluguel))
    print("Os dados foram armazenado no banco de dados!")

    conecta.commit()
    conecta.close()

#Registrar um aluguel, cliente X alugou filme Y
def registrar_aluguel(id_cliente: int, id_filme: int, devolvido: bool): #devolvido, False: nao devolvido. True: devolvido
    conecta = conectar()
    cur = conecta.cursor()

    cur.execute("INSERT INTO alugueis (id_cliente, id_filme, devolvido) VALUES (?, ?, ?)", (id_cliente, id_filme, devolvido))

    conecta.commit()
    conecta.close() 

#Calcular valor total de filmes alugados por cliente
def valor_total_filmes_alugados_por_cliente():
    conecta = conectar()
    cur = conecta.cursor()

    consulta = """
    SELECT clientes.id_cliente, clientes.nome, SUM(filmes.preco_aluguel) AS total_cliente FROM alugueis 
    JOIN clientes ON alugueis.id_cliente = clientes.id_cliente
    JOIN filmes ON alugueis.id_filme = filmes.id_filme
    GROUP BY clientes.id_cliente, clientes.nome
    ORDER BY total_cliente DESC
    """

    cur.execute(consulta)
    resultado = cur.fetchall()

    conecta.close()

    return resultado

#Listar todos os aluguéis com JOIN mostrando nome do cliente + título do filme
def listar_alugueis():
    conecta = conectar()
    cur = conecta.cursor()

    consulta = """
    SELECT clientes.nome, filmes.titulo FROM alugueis 
    JOIN clientes ON alugueis.id_cliente = clientes.id_cliente
    JOIN filmes ON alugueis.id_filme = filmes.id_filme
    """

    cur.execute(consulta)
    resultado = cur.fetchall() #mostra todas as linhas em tuplas

    conecta.close()

    return resultado
    
#Listar filmes alugados que ainda não foram devolvidos
def alugados_nao_devolvidos():
    conecta = conectar()
    cursor = conecta.cursor()

    sql = """
    SELECT filmes.titulo FROM alugueis 
    JOIN filmes ON alugueis.id_filme = filmes.id_filme
    WHERE devolvido = 0
    """

    cursor.execute(sql)
    resultado = cursor.fetchall() #exibe todas as linhas do SQL realizado com o cursor

    conecta.close()
    return resultado 

#Listar os 3 clientes que mais alugaram filmes
def listar_top3_clientes():
    conecta = conectar()
    cursor = conecta.cursor() 

    comando_sql = """
    SELECT clientes.nome
    FROM alugueis a 
    JOIN clientes ON a.id_cliente = clientes.id_cliente
    GROUP BY clientes.nome
    ORDER BY COUNT(a.id_filme) DESC
    LIMIT 3
    """

    cursor.execute(comando_sql)
    resultado = cursor.fetchall()

    conecta.close() #desativa o banco de dados
    return resultado 

#Atualizar status de devolução
def atualizar_status_devolucao(status, id_aluguel):
    conecta = conectar()
    cursor = conecta.cursor()
    
    comando_update = """
    UPDATE alugueis
    SET devolvido = ?
    WHERE id_aluguel = ?
    """

    cursor.execute(comando_update, (status, id_aluguel))
    print(f"O comando devolvido da tabela alugueis foi alterado para o status {status}")

    conecta.commit()
    conecta.close()

#Deletar cliente (com tratamento se tiver aluguéis ativos)
def deletar_cliente(id_cliente):
    conecta = conectar()
    cursor = conecta.cursor()

    alugueis_ativos = """
    SELECT COUNT(*) FROM alugueis
    WHERE id_cliente = ? AND devolvido = 0
    """
    cursor.execute(alugueis_ativos, (id_cliente,))
    pendentes = cursor.fetchone()[0]

    if pendentes > 0:
        print(f"Você possui {pendentes} alugueis pendentes, é necessário devolve-los antes de deletar o cliente solicitado")
        conecta.close()
        return 
    
    else:
        comando_delete = """
        DELETE FROM clientes WHERE id_cliente = ?
        """

        cursor.execute(comando_delete, (id_cliente,))
        
        if cursor.rowcount():
            print("Cliente deletado com sucesso! ")
        else:
            print("Nenhum cliete foi deletado (id nao encontrado)")
            
    conecta.commit()
    conecta.close()
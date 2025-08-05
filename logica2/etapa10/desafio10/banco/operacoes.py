# Funções que executam INSERT, SELECT, etc
from conexao import conectar 

#Inserir clientes e filmes via código Python
def inserir_clientes_filmes(nome: str, email: str, titulo: str, categoria:str, preco_aluguel:float):
    conecta = conectar()
    cur = conecta.cursor() 
    preco_aluguel = preco_aluguel.replace(",",".")

    cur.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", (nome, email))
    cur.execute("INSERT INTO filmes (titulo, categoria, preco_aluguel) VALUES (?, ?, ?)", (titulo, categoria, preco_aluguel))
    print("Os dados forão armazenado no banco de dados!")
    conecta.commit()
    conecta.close()

#Registrar um aluguel
def registrar_aluguel():
    conecta = conectar()
    cur = conecta.cursor()

    pass 

#Calcular valor total de filmes alugados por cliente
def valor_total_filmes_alugados_por_cliente():
    pass

#Listar todos os aluguéis com JOIN mostrando nome do cliente + título do filme
def listar_alugueis():
    pass

#Listar filmes alugados que ainda não foram devolvidos
def alugados_nao_devolvidos():
    pass

#Listar os 3 clientes que mais alugaram filmes
def listar_top3_clientes():
    pass

#Atualizar status de devolução
def atualizar_status_devolucao():
    pass

#Deletar cliente (com tratamento se tiver aluguéis ativos)
def deletar_cliente():
    pass

inserir_clientes_filmes("lui", "lui@gmail.com", "sereias", "ficção", "70.33")
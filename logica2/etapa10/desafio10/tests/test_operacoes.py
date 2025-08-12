# Testes com pytest
import sys
import os 
import pytest 

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) 
from banco.operacoes import *
from banco.conexao import conectar

def test_inserir_cliente():

    inserir_clientes("rayssa", "rayssa@gmail.com")
    
    consulta = """ SELECT nome, email FROM clientes WHERE email = 'rayssa@gmail.com' """
    conecta = conectar()
    cur = conecta.cursor()

    cur.execute(consulta)
    resultado = cur.fetchone()
    conecta.close()

    assert resultado is not None #confere se o resultado foi retornado
    assert resultado[0] == "rayssa"
    assert resultado[1] == "rayssa@gmail.com" #confere se o email retornado é o mesmo inserido

def test_registrar_aluguel():

    id_cliente = inserir_clientes("roberta", "roberta@gmail.com")
    id_filme = inserir_filmes("Os titãs", "desenho", 19)

    registrar_aluguel(id_cliente, id_filme, 0)
    
    consulta = """ SELECT clientes.id_cliente, filmes.id_filme
    FROM alugueis
    JOIN clientes ON alugueis.id_cliente = clientes.id_cliente
    JOIN filmes ON alugueis.id_filme = filmes.id_filme
    WHERE alugueis.id_cliente = ?"""

    conecta = conectar()
    cursor = conecta.cursor()

    cursor.execute(consulta, (id_cliente,))
    resultado = cursor.fetchone()
    conecta.close()

    assert resultado is not None 
    assert resultado[0] == id_cliente
    assert resultado[1] == id_filme

def test_alugado_nao_devolvido():
    inserir_clientes("luisa", "luisa@gmail.com")
    inserir_filmes("guerra nas estrelas", "ficcao", 38)

    conecta = conectar()
    cursor = conecta.cursor()

    cursor.execute("SELECT id_cliente FROM clientes WHERE nome = ?", ("luisa",))
    id_cliente = cursor.fetchone()[0]
    cursor.execute("SELECT id_filme FROM filmes WHERE titulo = ?", ("guerra nas estrelas",))
    id_filme = cursor.fetchone()[0]

    registrar_aluguel(id_cliente, id_filme, 0) #nao devolvido
    
    inserir_filmes("O cão leal", "fatos reais", 60)
    cursor.execute("SELECT id_filme FROM filmes WHERE titulo = ?", ("O cão leal",))
    id_filme2 = cursor.fetchone()[0]
    registrar_aluguel(id_cliente, id_filme2, 1)

    resultado = alugados_nao_devolvidos()
    titulo_filme = [titulo[0] for titulo in resultado]

    assert "guerra nas estrelas" in titulo_filme
    assert "O cão leal" not in titulo_filme
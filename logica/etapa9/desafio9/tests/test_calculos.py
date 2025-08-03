# Testes unitários reais (pytest)
import sys
import os 
import pytest 

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) #Cada .. é uma pasta a cima, __file__ é o local exato deste arquivo
from utils.calculos import *

def test_calcular_valor_total_estoque():
    valor = calcular_valor_total_estoque()
    arredondado = round(valor)

    assert arredondado > 0
    assert isinstance(valor, (float, int))
    assert valor > 0

def test_calcular_media_por_categoria(capsys): #pytest desafio9/tests/test_calculos.py::test_calcular_media_por_categoria

    retorna = calcular_media_por_categoria()
    capturar_print = capsys.readouterr().out #captura tudo que foi impresso e retorna uma tupla com (stdout, stderr) capturados e remove da tupla com o out
    
    esperado = {
        "Perifericos": 116,
        "Monitores": 1249,
        "Armazenamento": 186,
        "Cabos": 32
    }

    assert isinstance(retorna, dict)
    assert "------MEDIA DE PREÇOS POR CATEGORIA------" in capturar_print
    assert "Perifericos - R$ 116" in capturar_print
    assert "Monitores - R$ 1249" in capturar_print
    assert "Armazenamento - R$ 186" in capturar_print
    assert "Cabos - R$ 32" in capturar_print
    assert retorna == esperado  
    assert retorna["Monitores"] == 1249

def test_produto_mais_caro_mais_barato():
    caro, barato = variacao_preco()

    assert caro["produto"] == "Monitor Curvo 32"
    assert caro["preco"] == 1499.0
    assert barato["produto"] == "Cabo USB-C"
    assert barato["preco"] == 19.9

def test_ordenar_por_preco_decrescente(monkeypatch):
    entradas = iter(["preco", "True"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    resultado_alterado = ordenar_preco_quantidade() #executa a funcao com as respectivas entradas

    for item in resultado_alterado:
        assert isinstance(item["nome"], str)
        assert isinstance(item["categoria"], str)
        assert isinstance(item["quantidade"], int)
        assert isinstance(item["preco"], float)

#comando: pytest desafio9/tests/test_calculos.py::test_calcular_valor_total_estoque
#local: etapas\logica\etapa9> 

from desafio.diagnostico import verificar_impressao, verificar_visor, verificar_funcionamento_impressora
import pytest
import logging 

def test_output_verificarVisor_sim(monkeypatch, capsys): #Teste de Entrada/Saída
    #entrada do usuario simulada como sim
    monkeypatch.setattr("builtins.input", lambda _: "sim")

    verificar_visor()

    captura_impressao = capsys.readouterr()

    #verifica se é a mensagem que apareceu
    assert "Há erro no visor. O chamado tecnico foi efetivado para o concerto do visor, aguarde...." in captura_impressao.out

def test_output_verificarVisor_nao(monkeypatch, capsys): #Teste de Entrada/Saída

    monkeypatch.setattr("builtins.input", lambda _: "nao")

    verificar_visor()

    capturar_print = capsys.readouterr()

    assert "O visor da impressora está funcionando corretamente" in capturar_print.out


def test_impressora_logs(monkeypatch, caplog): #Verifica se os erros são corretamente registrados
    
    monkeypatch.setattr("builtins.input", lambda _: "abc")
    with caplog.at_level(logging.error):
        verificar_funcionamento_impressora()

        assert "Você deve digitar sim ou nao" in caplog.text
        

def test_impressao(monkeypatch, capsys): #Testa diferentes fluxos de entrada
    resposta = iter(["sim", "nao"])

    monkeypatch.setattr("builtins.input", lambda _: next(resposta))

    verificar_impressao()

    saida = capsys.readouterr()

    assert "quantidade de papeis verificada" in saida.out
#pytest test_diagnostico.py -s (roda o teste, se o usuario estiver na pasta desafio)
#pytest test_diagnostico.py::test_output_verificarVisor_nao -s
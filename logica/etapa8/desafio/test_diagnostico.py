from desafio.diagnostico import verificar_visor
import pytest

def test_output_verificarVisor_sim(monkeypatch, capsys):
    #entrada do usuario simulada como sim
    monkeypatch.setattr("builtins.input", lambda _: "sim")

    verificar_visor()

    captura_impressao = capsys.readouterr()

    #verifica se é a mensagem que apareceu
    assert "Há erro no visor. O chamado tecnico foi efetivado para o concerto do visor, aguarde...." in captura_impressao.out

def test_output_verificarVisor_nao(monkeypatch, capsys):

    monkeypatch.setattr("builtins.input", lambda _: "nao")

    verificar_visor()

    capturar_print = capsys.readouterr()

    assert "O visor da impressora está funcionando corretamente" in capturar_print.out

#pytest test_diagnostico.py -s (roda o teste, se o usuario estiver na pasta desafio)
#pytest test_diagnostico.py::test_output_verificarVisor_nao -s 
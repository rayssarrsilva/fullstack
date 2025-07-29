import diagnostico
import pytest

def test_output_verificarVisor(monkeypatch, capsys):
    #entrada do usuario simulada como sim
    monkeypatch.setattr("builtins.input", lambda _: "sim")

    diagnostico.verificar_visor()

    captura_impressao = capsys.readouterr()

    #verifica se é a mensagem que apareceu
    assert "Há erro no visor. O chamado tecnico foi efetivado para o concerto do visor, aguarde...." in captura_impressao.out

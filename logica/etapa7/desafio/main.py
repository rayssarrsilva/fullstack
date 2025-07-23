# Orquestra o sistema (Título, Score, Prioridade, Tempo aberto, Setor, Status + Estatísticas finais com base na função)
from entrada import entrada_chamados_tecnicos
from processamento import *

entrada = entrada_chamados_tecnicos()
calculo_score = calcular_score(entrada())
score_atribuido = atribuir_scores(calculo_score, entrada)
ordenacao_chamados = ordenar_chamados(score_atribuido)
status_classificado = classificar_status(ordenacao_chamados)
estatistica = analisar_estatisticas(ordenacao_chamados)

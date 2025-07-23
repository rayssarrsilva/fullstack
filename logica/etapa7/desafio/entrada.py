#coleta os dados a serem usados nos outros arquivos 

from typing import Dict, List, Union #Uniun: significa um ou outro

PRIORIDADE = ["baixa", "media", "alta"] #constante global de validação

def entrada_chamados_tecnicos() -> Dict[str, List[ Union[str, float]]]:
    """
    Coleta o titulo, prioridade do chamado, tempo resposta, tempo aberto e setor responsavel por meio de inputs

    Returns:
        Dict[str, List[ Union[str, float]]]: retorna um dicionario com cada chave seguida de seu valor que pode ser str ou float, tais valores armazenados em uma lista cada
    """
    print("Sistema de Coleta de Chamados - Início") #Usabilidade

    while True:
        try:
            chamados = int(input("Quantos chamados você deseja fazer? "))

            if chamados == 0:
                raise ValueError
            else:
                break 
        except ValueError:
            print("Voce deve inserir uma quantidade valida, maior que zero, de chamados")
    
    armazenamento = {
            "titulo": [],
            "prioridade": [],
            "tempo_resposta": [],
            "tempo_aberto": [],
            "setor_responsavel": []
        }
    
    for _ in range(chamados):
        titulo = str(input("Titulo do chamado: ")).strip()
        armazenamento["titulo"].append(titulo)

        while True:
            try: 
                prioridade = str(input("prioridade baixa, media ou alta? ")).lower().strip()

                if prioridade in PRIORIDADE:
                    armazenamento["prioridade"].append(prioridade)
                    break
                else:
                    raise ValueError

            except ValueError:
                print("A prioridade só pode ser baixa, media ou alta")
        
        tempo_resposta = float(input("Qual o tempo estimado para resolver o chamado (em horas)? "))
        tempo_aberto = float(input("Tempo em horas que o chamado está aberto até agora: "))
        setor_responsavel = str(input("Nome do setor que está responsável pelo chamado: ")).strip()

        armazenamento["tempo_resposta"].append(tempo_resposta)
        armazenamento["tempo_aberto"].append(tempo_aberto)
        armazenamento["setor_responsavel"].append(setor_responsavel) 

                
    return armazenamento

__all__ = ["entrada_chamados_tecnicos"]
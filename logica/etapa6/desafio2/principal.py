from codigo import *

def main():
    #inicia a funcao e salva em cada variavel o respectivo return
    nomes, glicose, colesterol, idade = entrada()

    g = glicose_alta(glicose)
    if g != 0:
        print(f"Existem {g} pacientes com glicose alta (acima de 99)")
    else:
        print(f"Nenhum paciente possui glicose alta")
    
    colesterol_a = colesterol_acima(colesterol)
    if colesterol_a > 0:
        print(f"Existem {colesterol_a} paciente com a colesterol acima de 200")
    else:
        print("Nenhum paciente possui colesterol alto")
    
    nome, _ = nome_paciente(nomes, glicose)
    print(f"O nome do paciente com o maior indice de glicose é {nome}")

    mg4, mc4, mg6, mc6, mgm, mcm = medir(glicose, colesterol, idade)
    print("-----MEDIA DE COLESTEROL E GLICOSE POR IDADE-----")
    print(f"Abaixo de 40: media glicose - {mg4}; media colesterol - {mc4}")
    print(f"40-60: media glicose - {mgm}; media colesterol - {mcm}")
    print(f"Acima de 60: media glicose - {mg6}; media colesterol - {mc6}")

    lista_nomes = acompanhamento(nomes, glicose, colesterol)

    if not lista_nomes: #se lista vazia
        print("Nenhum paciente precisa de acompanhamento médico") 
    else:
        for nome in lista_nomes:
            print(f"{nome} - Precisa de acompanhamento médico")

    print("-----RESUMO CLINICO-----")
    resumo_clinico(nomes, glicose, colesterol, idade)

if __name__ == "__main__":
    main()
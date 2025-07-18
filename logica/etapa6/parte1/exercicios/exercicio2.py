# Sistema de Controle de Estoque de Medicamentos
#Uma clínica precisa de um sistema simples para verificar o estado do seu estoque de medicamentos.

"""🧾 Regras:
Crie duas listas paralelas:

nomes = [...] → nomes dos medicamentos.

estoques = [...] → quantidades respectivas.

Use funções como len(), sum(), min(), e estruturas de controle for, if.

O foco é aplicar lógica algorítmica com clareza e simular um sistema prático.

"""

nomes = ["Ibuprofeno", "Dimeticona", "Loratadina", "Paracetamol", "Omeprazol", "Clorexidina", "Dexclorfeniramina"]
estoques = [12, 32, 44, 53, 11, 64, 78]

def total_medicamentos():
    total_medicamentos = sum(estoques)
    return total_medicamentos

def quantidade_media_medicamento():
    quantidade_media_medicamento = sum(estoques)/len(estoques)
    return quantidade_media_medicamento

def quantidade_minima():
    minima = min(estoques)
    return minima 

def nomear_quantidade_menor():
    for nome, valor in zip(nomes, estoques):
        if valor == min(estoques):
            return nome 

def valor_abaixo_cinquenta():
    abaixo_cinquenta = len([remedio for remedio in estoques if remedio < 50])
    return abaixo_cinquenta


def nomear_valores_menores():
    reposicao = []
    for nome, valor in zip(nomes, estoques):
        if valor < 50:
            reposicao.append(nome)
    return reposicao

Nome = nomear_valores_menores()

print(f"O total de medicamentos disponíveis no estoque é {total_medicamentos()}")
print(f"A quantidade média no estoque por medicamento é {quantidade_media_medicamento()}")      
print(f"A quantidade mínima é {quantidade_minima()} e o nome do medicamento com menor estoque é {nomear_quantidade_menor()}")
print(f"A quantidade de medicamentos com estoque abaixo de 50 unidades é {valor_abaixo_cinquenta()}")
print(f"O nome dos medicamentos que precisam de reposição é ")
for nome in Nome:
    print(nome)

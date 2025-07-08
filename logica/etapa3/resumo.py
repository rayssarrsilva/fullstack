# Listas (arrays, vetores) - coleções ordenadas da entrada (Lista --> Variavel = [])
frutas = ["maçã", "banana", "uva"]
print(frutas[0])  # maçã

frutas.append("laranja")   # adiciona
frutas.remove("banana")    # remove
frutas.sort()              # ordena
frutas.reverse()           # inverte

#Tuplas (Tupla --> Variavel = ()), imutáveis, não mudam depois de criadas. Usadas para representar dados fixos (ex: coordenadas, CPF, datas) e mais rápidas

ponto = (2, 3)

#Sets/Conjuntos (Set/Conjunto --> Variavel = set()) Output --> {1 caractere unico de todos os inseridos no conjunto}. Remover duplicatas, Testar pertinência (in), Operações matemáticas: união, interseção, diferença

variavel = set("rayssa")
print(variavel)
letras = set("banana")
print(letras)  # {'b', 'a', 'n'}

#Dicionários, são chave-valor

pessoa = {
    "nome": "Rayssa",
    "idade": 25
}
print(pessoa["nome"])  # Rayssa

pessoa.get("email", "Não cadastrado") #chave que se deseja procurar, valor que se retorna caso nao encontre o valor da respectiva chave procurada
pessoa.keys()
pessoa.values()

#Pilhas/Stacks (Pilha/Stack --> Variavel = []) - Last in, First Out. Histórico de navegação e Undo/Redo em editores

pilha = []
pilha.append("Arroz")
pilha.append("Banana")
print(pilha)
print(pilha[-1]) #primeiro
print(pilha.pop())  # B

#Filas/Queues First in First Out (Filas/Queues --> from collections import deque    Variavel = deque()) - Primeiro a entrar e primeiro a sair. Output --> ([])

from collections import deque
fila = deque()

fila.append("Amor")
fila.append("B")
print(fila)
print (fila[0]) #primeiro
print(fila.popleft())  # A

#Tabelas Hash armazenam dados com acesso rápido por chave

# Estruturas Mistas (listas dentro de dicionários, etc.)
agenda = {
    "segunda": ["reunião", "academia"],
    "terça": ["curso"]
}

print(agenda)

for dia, atividade in agenda.items():
    print(f"{dia} é dia de ")
    for atividades in atividade: #itera sobre a lista desenvolvida dentro dos valores das chaves da semana
        print(f" {atividades}")

print(agenda.get("segunda"))
print(agenda.get("quarta", "dia nao encontrado"))

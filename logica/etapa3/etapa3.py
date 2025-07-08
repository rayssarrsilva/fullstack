#Crie um dicionário de contatos com nome e número. Permita buscar pelo nome.

def contatos():

    print("ATENÇÃO: Digite sair caso não queira salvar um contato")

    contatos = {}

    while True:
        nome = input("nome: ").lower()

        if nome in ("sair"):
            break
        else:
            numero = int(input("número: "))
            contatos[nome] = numero


    print("------Buscador de CONTATOS------ (digite parar)")
    while True:

        buscar = input("Qual nome você deseja buscar nos contatos? ").lower()

        if buscar in contatos:
            print(f"O numero de {buscar} está salvo, o número é {contatos.get(buscar)}")
        elif buscar == "parar":
            break
        else:
            print("Voce não salvou esse número")

# Simule uma fila de atendimento com 5 pessoas. Mostre a ordem e quem será atendido primeiro.

def fila_atendimento():

    from collections import deque
    fila = deque() #primeiro a entrar e primeiro a sair

    for pessoa in range(0, 5):
        nome = input("Qual o nome da pessoa a ser atendida? ").strip().title()
        fila.append(nome)

    print("A ordem de atendimento será: ")
    for pessoa in fila:
        print(pessoa)

    print(f"O primeiro a ser atendido será {fila[0]}")


#Implemente uma pilha de páginas visitadas e mostre o comportamento do botão “voltar”.

def paginas():

    historico = []

    while True:
        pagina = input("Deseja acessar algum site? (Ou deseja 'voltar'/'sair') ").lower()

        if pagina == "sair":
            break
        elif pagina == "voltar":
            if not historico: #True: não está vazio / Not true: vazio
                print("Você não pode voltar mais - HISTORICO VAZIO")
            else:
                print(f"voltando para {historico.pop()}")
        else: 
            historico.append(pagina)


#Crie uma lista com 15 números, remova os repetidos e exiba os únicos em ordem crescente.

def lista_sem_repetidos():
    lista = [ 1, 2, 3, 6, 5, 6, 7, 8, 3, 10, 10, 12, 13, 10, 1 ]
    ordenar = sorted(lista) #função de ordem crescente

    repetidos = set(ordenar) #função pra remover os repetidos (usado pra criar set e conjuntos)

    print(repetidos)
    
# Monte uma estrutura com 3 dias da semana e atividades do dia (dicionário com listas). Mostre tudo com for.

def mostrar_dias_atividades():
    dicionario = {
        "segunda": ["nadar", "cozinhar", "massagista"],
        "terça": ["pular corda", "estudar", "editar"],
        "sábado": ["pintar", "jogar xadrez", "tocar piano"]
    }

    for dia, atividade in dicionario.items(): #chave/[] 
        print(f"{dia}: ")
        for atividades in atividade: #[valores, iterados]
            print(f"- {atividades}")

def dic_input():
    semana_atividade = {}

    for dias in range(2):
        atividades = [] #reseta a atividade a cada dia da semana digitado

        semana = input("Qual dia da semana deseja inserir? ").title()
        quantidade_atv = int(input("quantas atividades você fez nesse dia? "))

        for atividade in range(quantidade_atv):
            atv = input(f"Atividade {atividade+1}: ")
            atividades.append(atv) #salva as atividades dentro da lista criada pra salvar novos valores a cada dia, ao invez de acumular.

        semana_atividade[semana] = atividades #debug: {} -> {chave:} -> {chave: valor} /a cada dia da semana salva apenas as atividades do respectivo dia 

    print(semana_atividade)

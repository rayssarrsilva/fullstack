# Sistema: Gerador de Relatórios de Estudos

"""
Adicionar try/except para validar entradas e lidar com erros (CHECK) - Evitar que o programa quebre com entradas erradas	
.join() - exibir ou salvar vários dados formatados. CHECK
open("arquivo.txt", "w") - serve para logs, criação, manipulação e exportação de arquivos. CHECK
main() e __name__ - arquitetura modular, onde o main pode ser executado diretamente, como um programa em si ou até mesmo ser importado por outro modulo! - Se você não usar main(), o programa vai rodar tudo assim que importar
Substituir as tuplas por Dicionário (legibilidade e escalabilidade). CHECK
Testabilidade
"""

def nomear_usuario(): #padrao de nomeação verbal

    while True:
        try:
            nome = input("Digite seu nome: ").strip()
            if nome.isalpha():
                return nome 
        except TypeError:
            print("TypeError: Digite seu nome")

""" A função nomear_usuario cria um loop para que a cada except o input seja retornado novamente, se o valor inserido for alfabetico entao é retornado o nome pela função."""

def gerar_relatorio(): 
    
    lista_dicionario = [] #evita quebra de isolamento das funções ao usar variavel interna/escopo

    while True:
        try:
            dias = int(input("Quantos dias de estudo deseja registrar? "))
            break
        except (ValueError, TypeError): 
            print("Error: Insira um número inteiro")

    for dia in range(dias):
        print(f"---Dia {dia+1}---")
        
        while True:
            try:
                dia_semana = input("Dia da semana: ").strip()
                if dia_semana.isalpha():
                    break
                else:
                    raise TypeError
            except (TypeError):
                print("TypeError: digite o dia da semana.")
            
        while True:
            try:
                atividade = input("Atividade: ").title()
                if atividade.isalpha():
                    break
                else:
                    raise TypeError("TypeError")
            except (TypeError) as error:
                print(f"{error}: digite a atividade realizada.")

        while True:
            try:
                horas_estudadas = input("Horas estudadas: ")
                if horas_estudadas.isdigit():
                    horas_estudadas = int(horas_estudadas)
                    break
                else:
                    raise TypeError("TypeError")
            except (TypeError) as error:
                print(f"{error}: digite a quantidade de horas estudadas.")

        dicionario = {"dia_semana": dia_semana, "atividade": atividade, "horas_estudadas": horas_estudadas}
        lista_dicionario.append(dicionario) 


    return lista_dicionario

"""Cria uma lista interna que armazena os valores do dicionario
Usa try/except dentro de whiles, para cada entrada de dados, permitindo que o input seja solicitado novamente a cada except.
1. Try - se o valor inserido for int, ele da break no laço True e passa para o próximo código. Except: Se der except é um valueerror ou typeerror.
2. Try - se o valor inserido for alfabetico ele para, se nao raise um TypeError e um except da mesma categoria que se repete no laço e da break caso seja uma letra.
3. Try - Faz o mesmo que o 2
4. Try - se o valor digitado for um digito numerico, converte ele pra inteiro e da break para terminar o laço e repetir caso o for nao tenha terminado ainda. Se não da raise TypeError e except da mesma categoria.
Cria uma variavel dicionario dentro do for para salvar todos os inputs com chaves pré definidas.
Adiciona a variavel que salva os valores do dicionario na lista.
Da um return da lista, a qual serve como retorno ao chamarem essa função.
"""

def calcular_total(parametro):

    lista = [] 
    for itens in parametro: 
        lista.append(itens['horas_estudadas'])

    total = sum(lista)
    return total 

"""A função calcular_total, cria uma variavel interna fora do loop usada como Lista, para salvar todas as horas_estudadas iteradas.
Possui 1 parametro onde é inserido a lista de tuplas, lista de dicionarios, lista, ou qualquer coisa iteral.
Usa apenas uma variavel de controle pois se trata de uma lista de dicionarios, logo é usado a chave para especificar do que se trata e não a ordem.
Armazena a soma dos valores da lista dentro da variavel total e retorna esse valor ao chamar a função."""

def salvar_relatorio(nome, ListaCompleta):
    try:
        with open("relatorio.txt", "x") as arquivo:
            arquivo.write(f"{nome} \n")
            arquivo.write(f"{ListaCompleta} \n")
    except FileExistsError:
            with open("relatorio.txt", "a") as arquivo:
                arquivo.write(f"{nome} \n")
                arquivo.write(f"{ListaCompleta} \n")

""" A função salvar_relatorio, salva 2 parametros quaisquers.
Try - cria o arquivo relatorio.txt com X (cria e gera erro caso ja existir)
except - Da o erro de FileExistsError, trocando o X pelo A, que apenas faz o append dos parametros sem substituir ou criar arquivos."""

def exibir_relatorio():
    nome = nomear_usuario()
    dados = gerar_relatorio()
    total_horas = calcular_total(dados)
    
    dados_relatorio = []

    print(f"Relatorio de estudos - {nome}")
    for item in dados:
        relatorio = f" {item['dia_semana']} - {item['atividade']} - {item['horas_estudadas']}h"
        dados_relatorio.append(relatorio)

    relatorio_horas = f"E o total de horas feitas foi {total_horas}h"
    dados_relatorio.append(relatorio_horas)

    formatar = "\n".join(dados_relatorio)

    print(formatar)

    salvar_relatorio(nome,formatar)

"""Join - salva todas as f strings em uma variavel e insere elas em uma lista, que sera formatada com virgulas usando join
Dicionario - usa apenas uma variavel iteradora para iterar sobre a lista que contém o dicionário """

if __name__ == "__main__":
    exibir_relatorio()

"""Executa apenas a/as funções que estão dentro do main, inclusive ao ser importado
ATENÇÃO: Evita que todas as funções sejam executadas automaticamente, ao serem importadas! """
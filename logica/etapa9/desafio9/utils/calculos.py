# Funções como calcular total, média, menor, maior, etc.
import csv 
from typing import Dict, List, Union
import os 
CAMINHO_CSV = os.path.join(os.path.dirname(__file__), '..', 'estoque.csv') #localiza o arquivo atual, sobe 1 pasta e acessa o arquivo estoque.csv

#Calcula valor total do estoque
def calcular_valor_total_estoque() -> float: 
    valor_total = 0
    with open(CAMINHO_CSV, mode='r', newline='', encoding='utf-8') as estoque:
        ler = csv.DictReader(estoque)

        for item in ler:
            quantidade = int(item['quantidade'])
            preco = float(item['preco'])
            valor_total += quantidade * preco  

    arredondado = round(valor_total)

    print(f"O VALOR TOTAL DO ESTOQUE ARREDONDADO É R$ {arredondado}")

    return valor_total

#Calcula média de preço por categoria
def calcular_media_por_categoria() -> Dict[str, int]:
    dicionario = {}
    relatorio = {}

    with open(CAMINHO_CSV, mode='r', newline='', encoding='utf-8') as arquivo:
        ler = csv.DictReader(arquivo)

        for produto in ler:
            quantidade = int(produto['quantidade'])
            categoria = str(produto['categoria'])
            preco = float(produto['preco'])

            if categoria not in dicionario:
                dicionario[categoria] = {'preco': 0, 'quantidade': 0} #inicializa a criação das chaves internas do dicionario para cada categoria

            #acumula os valores dentro do dicionario na respectiva chave
            dicionario[categoria]['preco'] = dicionario[categoria]['preco'] + (preco * quantidade) 
            dicionario[categoria]['quantidade'] = dicionario[categoria]['quantidade'] + quantidade

    for categoria, item in dicionario.items():
        media = (item['preco'] /item['quantidade'])

        relatorio[categoria] = round(media)

    #exibe de forma visualmente agradavel para o usuario
    print("------MEDIA DE PREÇOS POR CATEGORIA------")
    for categoria, preco in relatorio.items():
        print(f"{categoria} - R$ {preco}")

    return relatorio 


#Mostra produto mais caro e mais barato
def variacao_preco() -> float:
    caro = None 
    barato = None

    with open(CAMINHO_CSV, mode='r', newline='', encoding='utf-8') as arquivo:
        ler = csv.DictReader(arquivo)

        for categoria in ler:
            nome = categoria['nome']

            preco = float(categoria['preco'])

            if caro is None or preco > caro['preco']:

                caro = {'produto': nome, 'preco': preco}
            
            if not barato:
                barato = {'produto': nome, 'preco': preco}
            else:
                if preco < barato['preco']:
                    barato = {'produto': nome, 'preco': preco}

    print("---PRODUTO MAIS CARO---")

    for produto, preco in caro.items():
        print(f"{produto}: R$ {preco}")

    print("---PRODUTO MAIS BARATO---")

    for produto, preco in barato.items():
        print(f"{produto}: R$ {preco}")

    return caro, barato 

#Ordena produtos por preço ou quantidade
def ordenar_preco_quantidade() -> List[Dict[str, Union[str, int] ]]:

    print("-----SISTEMA PARA ORDENAR PRODUTOS PELO PREÇO OU QUANTIDADE-----")
    with open(CAMINHO_CSV, mode='r', newline='', encoding='utf-8') as arquivo:
        ler = csv.DictReader(arquivo)
        convertido = list(ler) #salva na memoria e pode usar quantas vezes quiser
        for item in convertido:
            item["quantidade"] = int(item["quantidade"])
            item["preco"] = float(item["preco"])   

    while True:
        try:
            ordenar = input("Você deseja ordenar por preco ou quantidade (quit)? ").lower()
            if ordenar not in ["preco", "quantidade", "quit"]:
                raise ValueError
            
            elif ordenar == 'quit':
                print("Encerrando sistema...")
                break

            else: 
                while True:
                    try:
                        ordem = input("Deseja ordenar por ordem decrescente (True/False)? ").capitalize()
                        if ordem not in ["True", "False"]:
                            raise ValueError
                        else: 
                            if ordem == "True":
                                ordem = True 
                            else:
                                ordem = False 
                            break 

                    except ValueError:
                        print("ERROR: digite True ou False")

                if ordenar == "preco":
                    preco_ordenado = sorted(convertido, key=lambda x: float(x['preco']), reverse=ordem)

                    for item in preco_ordenado:
                        print(f"{item['nome']} - Categoria: {item['categoria']} - Preco: {item['preco']} - Quantidade: {item['quantidade']}")
                        
                    return preco_ordenado
                else:
                    quantidade_ordenada = sorted(convertido, key= lambda x: int(x['quantidade']), reverse=ordem)

                    for item in quantidade_ordenada:
                        print(f"{item['nome']} - Categoria: {item['categoria']} - Preco: {item['preco']} - Quantidade: {item['quantidade']}")
                        
                    return quantidade_ordenada
        except ValueError:
            print("ATENÇÃO: você só pode ordenar por quantidade ou preco")

__all__ = ["calcular_valor_total_estoque","calcular_media_por_categoria","variacao_preco","ordenar_preco_quantidade"]
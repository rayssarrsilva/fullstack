
def cadastrar_transacoes() -> int:
    """ Solicita o número de transações que o úsuario deseja fazer """
    quantidade: int = int(input("Digite o número de transações: "))
    return quantidade 

def cadastrar_valor_transacao() -> float:
    """ Solicita o valor da transação com tratamento de erro para caso o usuario digite algo que nao seja númerico"""
    while True:
        try:
            valor = float(input("Digite o valor da transação: ").strip())
            return valor
        except ValueError: 
            print("ValueError: Digite um número válido")

def registrar_tipo() -> str:
    """ Oferece 2 opções listadas dentro de uma lista para o usuário registrar o tipo da transação (entrada/saida)"""
    opcoes = ["entrada", "saida"]
    while True:
        try:
            tipo: str = input("Digite o tipo (entrada/saida): ").lower()
            if tipo in opcoes:
                return tipo
            else:
                raise ValueError("Digite um dos tipos exigidos (Entrada/Saida)")
        except ValueError as Value:
            print(Value)

def registrar_categoria() -> str: #indica o tipo do valor que a função vai retornar
    """ Solicita a categoria da transação e retorna ao chamarem a função """
    while True:
        categoria: str = input("Digite a categoria da transação: ").lower() #indica o tipo da variável
        
        if categoria: #Vazia = False/Preenchida = True
            return categoria
        else:
            print("A categoria não pode estar vazia, digite a categoria da transação")

from typing import List, Dict

def coletar_dados_transacoes() -> List[Dict[str, float|int|str ]]:
    """ Coleta os dados solicitados por todas as respectivas funções e salva eles em um dicionário dentro de uma Lista"""
    quantidade = cadastrar_transacoes()

    armazenamento = []
    for transacao in range(quantidade):
        print(f"TRANSAÇÃO {transacao+1}")

        valor = cadastrar_valor_transacao()
        tipo = registrar_tipo()
        categoria = registrar_categoria()

        armazenamento.append({"valor": valor, "tipo": tipo, "categoria": categoria}) #cria um dicionario dentro da lista, com suas respectivas chaves.
    return armazenamento



""" Definem as funções que podem ser expostas ao usar: from entrada_transacoes import * """
__all__ = [ 
    "cadastrar_transacoes",
    "cadastrar_valor_transacao",
    "registrar_tipo",
    "registrar_categoria",
    "coletar_dados_transacoes"
]

#if __name__ == "__main__": #Evita que tudo que estiver fora de funções será executado automaticamente
    #print(coletar_dados_transacoes())


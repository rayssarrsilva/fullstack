from desafio9.utils.calculos import (
    calcular_valor_total_estoque,
    calcular_media_por_categoria,
    variacao_preco,
    ordenar_preco_quantidade
)

def main():
    calcular_valor_total_estoque() #Executa calculo do valor total do estoque e arredonda

    calcular_media_por_categoria() #imprime a media de preços por categoria

    variacao_preco() #imprime o produto mais caro e seu preco, seguido do produto mais barato e seu preço

    ordenar_preco_quantidade() #sistema que ordena produtos por preço ou quantidade em ordem crescente ou descresente  

if __name__ == "__main__":
    try:
        main()
    except Exception as erro:
        print(f"ERRO: {erro}")
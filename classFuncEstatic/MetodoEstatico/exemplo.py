class Produto:
    @staticmethod
    def aplicar_desconto(valor: float, desconto: float) -> float:
        return valor - (valor * desconto)
    
    @staticmethod
    def somar_produto(*valores) -> float:
        return sum(valores)

produto = Produto() #instancia sem atributos

print(f"Desconto de {Produto.aplicar_desconto(50, 2)}")
print(f"A soma dos produtos é {produto.somar_produto(2, 3, 4, 5)}")

class MinhaClasse:
    @staticmethod
    def meu_metodo_estatico(parametro):
        return f"Este é um método estático com o parâmetro: {parametro}"

print(MinhaClasse.meu_metodo_estatico("abc"))


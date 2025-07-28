class Produto:
    def __init__(self, nome: str, preco: float, estoque: int):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def calcular_total(self):
        return self.preco * self.estoque


p1 = Produto("Camisa", 50.0, 10) #estado do objeto p1 
print(p1.calcular_total())  # 500.0

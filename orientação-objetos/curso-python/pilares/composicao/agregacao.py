#É uma especialização da associação, uma coisa TEM outra coisa

class Carrinho:
    def __init__(self):
        self._produtos = []

    def colocar_no_carrinho(self,*produtos):
        self._produtos.extend(produtos)
        # self._produtos+= produtos # Funciona Igual

    def valor_total(self):
        return sum(p.valor for p in self._produtos)

    def listar_produtos(self):
        for p in self._produtos:
            print(f"-{p.nome}: R${p.valor}")

class Produto:
    def __init__(self,nome:str,valor:float):
        self.nome = nome
        self.valor = valor


carrinho_verde = Carrinho()

laranja = Produto("Laranja",4.0)
leite = Produto("Leite",5.0)   

carrinho_verde.colocar_no_carrinho(laranja,leite)
carrinho_verde.listar_produtos()
print(carrinho_verde.valor_total())


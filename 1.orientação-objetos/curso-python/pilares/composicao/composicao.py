# É uma especialização da agregação

class Cliente:
    def __init__(self, nome:str) -> None:
        self.nome = nome
        self.produtos = []
    
    def inserir_produto(self, nome, valor, qntd) -> None:
        self.produtos.append(Produto(nome,valor,qntd)) # Diferente da agregacao aqui os objetos so existem quando é chamado o metodo, e se eu apagar o cliente com um del, os objetos de Produto que foram instanciados aqui tambem irao ser apagados pelo garbage collector
        print(f"Produto {nome} adicionado!")

    def inserir_produto_exterto(self,*produtos):
        self.produtos.extend(produtos)

    def valor_total(self):
        valor_total = 0
        for i in range(len(self.produtos)):
            valor_total += self.produtos[i].valor * self.produtos[i].qntd
        return valor_total
    
    def listar_produtos(self):
        for item in self.produtos:
            print(item)
    
    def __del__(self):
        print(f"Apagando Objeto da Classe Cliente: {self.nome}")


class Produto:
    def __init__(self,nome:str,valor:float,qntd) -> None:
        self.nome = nome
        self.valor = valor
        self.qntd = qntd
    
    def __str__(self) -> str:
        return f"{self.nome} // {self.valor} // {self.qntd} // total:{self.valor*self.qntd}"
    
    def __del__(self):
        print(f"Apagando objeto da Classe Produto: {self.nome}")

cliente1 = Cliente("Davi")
produto_externo = Produto("Banana",1,1)

cliente1.inserir_produto("Cereal",5.0,5)
cliente1.inserir_produto("Leite",2,10)
cliente1.inserir_produto_exterto(produto_externo)
cliente1.listar_produtos()

del cliente1

print("Fim do programa")

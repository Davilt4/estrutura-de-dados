class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
class Pilha:
    def __init__(self):
        self.__topo = None
        self.__tamanho = 0

    def vazia(self):
        return self.__tamanho == 0

    def empilhar(self, dado):
        no = No(dado)
        no.proximo = self.__topo
        self.__topo = no
        self.__tamanho += 1

    def desempilhar(self):
        if self.__topo is None:
            raise Exception("Pilha vazia")
        valor = self.__topo.dado
        self.__topo = self.__topo.proximo
        self.__tamanho -= 1
        return valor
    
    def inverter(self):
        if self.vazia():
            raise Exception("Pilha vazia")
        
        pilha_auxiliar = Pilha()

        while not self.vazia():
            pilha_auxiliar.empilhar(self.desempilhar())

        self = pilha_auxiliar
    
    def __str__(self):
        elementos = ""
        elemento = self.__topo
        while elemento is not None:
            if elemento.proximo is None:
                elementos += str(elemento.dado)
            else:
                elementos += f"{elemento.dado} -> "
            elemento = elemento.proximo
        return elementos


pilha1 = Pilha()
pilha1.empilhar(1)
pilha1.empilhar(2)
pilha1.empilhar(3)
pilha1.empilhar(4)
pilha2 = Pilha()
pilha2.empilhar(5)
pilha2.empilhar(6)
pilha2.empilhar(7)
pilha2.empilhar(8)
print(pilha1)
pilha1.inverter()
print(pilha1)
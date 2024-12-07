import time

inicio = time.time()
class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None
        self.cauda = None
        self.tamanho = 0


    def adicionar_inicio(self, valor):
        no = No(valor)
        if self.cabeca is None:
            self.cabeca = no
            self.cauda = no
        else:
            no.proximo = self.cabeca
            self.cabeca = no
        self.tamanho += 1    
        return self.tamanho
    
    def adicionar_fim(self, valor):
        no = No(valor)
        if self.cabeca is None:
            self.cabeca = no
            self.cauda = no
        else:
            self.cauda.proximo = no
            self.cauda = no
        self.tamanho += 1    
        return self.tamanho


lista = ListaEncadeada()
for i in range(100000):
    lista.adicionar_fim(i)
lista.adicionar_inicio(0)
for i in range(100000):
    lista.adicionar_inicio(i)
fim = time.time()
print(fim - inicio)
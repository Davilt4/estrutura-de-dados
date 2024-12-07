class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._numero_de_paginas = 0
        self._caneta = None

    @property
    def caneta(self):
        return self._caneta

    @caneta.setter
    def caneta(self,caneta):
        self._caneta = caneta 

class Caneta:
    def __init__(self, marca):
        self.marca = marca


escritor1 = Escritor("Davi")
caneta1 = Caneta("BIC")

escritor1.caneta = caneta1
print(escritor1.caneta)

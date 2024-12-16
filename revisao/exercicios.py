
#Implemente o método para inverter a pilha.
def inverter(self):
    if self.vazia():
        raise(PilhaVaziaException)
    
    pilha_auxiliar = Pilha()

    while not self.vazia():
        pilha_auxiliar.empilhar(self.desimpilhar())

    while not pilha_auxiliar.vazia():
        self.empilhar(pilha_auxiliar.desempilhar())


#Implemente o método para checar_duplicidade da lista.
def checar_duplicidade(self):
    elementos_vistos = set()
    elemento = self.cauda
    while elemento is not None:
        if elemento.valor in elementos_vistos:
            return True
        elementos_vistos.add(elemento.valor)
        elemento = elemento.proximo
    return False
  

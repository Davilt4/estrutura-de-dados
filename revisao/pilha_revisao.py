#Implemente o método para inserir um elemento na pilha.
def inserir(self,valor):
    no = No(valor)
    no.proximo = self.topo
    self.topo = no
    tamanho += 1

#Implemente o método para remover um elemento na pilha.
def remover(self):
    if self.vazia():
        raise(PilhaVaziaException)
    valor = self.topo.valor
    self.topo = self.topo.proximo
    self.tamanh0 -= 1
    return valor

#Implemente o método para obter um elemento da posição X da pilha.
def obter_elemento(self,posicao):
    if posicao > self.tamanho - 1:
        raise (IndexError)
    elemento = self.topo
    posicao_elemento = 0
    while elemento is not None:
        if posicao_elemento == posicao:
            return elemento.valor
        posicao_elemento += 1
        elemento = elemento.proximo

#Implemente o método para inverter a pilha.
def inverter(self):
    pilha_auxiliar = 

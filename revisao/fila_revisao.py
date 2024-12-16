#Implemente o método para inserir um elemento na fila.
def inserir(self,valor):
    no = No(valor)
    if self.vazia():
        self.primeiro = no
        self.ultimo = no
    else:
        self.ultimo.proximo = no
        self.ultimo = no
    self.tamanho += 1

# Implemente o método para remover um elemento na fila.
def remover(self):
    if self.vazia():
        raise (FilaVaziaException)
    valor = self.primeiro.valor
    self.primeiro = self.primeiro.proximo
    self.tamanho -= 1
    return valor

#Implemente o método para imprimir os elementos da fila
def __str__(self):
    elementos = ""
    elemento = self.primeiro
    while elemento is not None:
        if elemento.proximo is None:
            elementos += str(elemento.valor)
        else:
            elementos += f"{elemento.valor} -> "
        elemento = elemento.proximo
    return elementos

#Implemente o método para concatenar para a fila.
def concatenar(self,fila2):
    if fila2.vazia():
        raise(FilaVaziaException)
    while not fila2.vazia():
        self.enfileirar(fila2.desinfileirar())

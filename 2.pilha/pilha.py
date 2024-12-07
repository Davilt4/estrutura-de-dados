class Pilha:
    def __init__(self):
        self.__items = []

    def empilhar(self,item):
        self.__items.append(item)
    
    def desimpilhar(self) -> int:
        if self.esta_vazia:
            print("A pilha esta vazia")
            return
        return self.__items.pop()
    
    def __str__(self):
        return str(self.__items)

    def __len__(self):
        return self.tamanho

    @property
    def esta_vazia(self):
        return len(self.__items) == 0
    
    @property
    def esta_cheia(self) -> bool:
        return False
    
    @property
    def tamanho(self):
        return len(self.__items)
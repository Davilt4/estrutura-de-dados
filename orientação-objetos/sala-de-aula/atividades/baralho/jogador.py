class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.__mao = []

    def __str__(self):
        return f"{self.nome} tem {len(self.__mao)} cartas"
    
    def add_carta(self, carta):
        self.__mao.append(carta)
    
    def inserir_carta(self, carta):
        self.__mao.insert(0, carta)

    def mostrar_mao(self):
        print(F"Cartas de {self.nome}:")
        for carta in self.__mao:
            print(f"{carta}")
        print()

    def len_mao(self):
        return len(self.__mao)

    def puxar_carta(self):
        return self.__mao.pop()
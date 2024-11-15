from carta import Carta

class Baralho:
    valor_das_cartas = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Valete": 11, "Dama": 12, "Rei": 13}

    def __init__(self): # método construtor e cria o baralho
        self.__cartas = []
        for naipe in ["Ouros", "Espadas", "Copas", "Paus"]:
            for valor in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valete", "Dama", "Rei"]:
                self.__cartas.append(Carta(valor, naipe))

    def embaralhar(self): 
        import random
        random.shuffle(self.__cartas)
    
    def distribuir_cartas(self, *jogadores, qtd_cartas):
        for jogador in jogadores:
            for i in range(qtd_cartas):
                jogador.add_carta(self.__cartas.pop()) # Alé de adionar cartas na mao, tambem remove a carta do baralho
    
    def __str__(self):
        return f"Baralho com {len(self.__cartas)} cartas"
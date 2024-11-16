import os
import time
from baralho import Baralho
from jogador import Jogador

#Batalha simulada com apenas 2 jogadores

class Batalha:
    def __init__(self):
        self.baralho = Baralho()
        self.jogador1 = Jogador("Jogador 1")
        self.jogador2 = Jogador("Jogador 2")
        self.jogadores = [self.jogador1, self.jogador2]
    
    def iniciar_batalha(self):
        print("Batalha iniciada!")
        print("Embaralhando cartas...")
        # time.sleep(1)
        self.baralho.embaralhar()
        print("Distribuindo cartas...")
        # time.sleep(1)
        self.baralho.distribuir_cartas(self.jogador1, self.jogador2, qtd_cartas=26)
        
    def rodada(self):
        cartas_empate = []
        print("Rodada iniciada!")
        print("Jogador 1 puxa carta...")
        # time.sleep(1)
        carta_jogador1 = self.jogador1.puxar_carta()
        print(f"Carta puxada: {carta_jogador1}")
        print("Jogador 2 puxa carta...")
        # time.sleep(1)
        carta_jogador2 = self.jogador2.puxar_carta()
        print(f"Carta puxada: {carta_jogador2}")
        print("Comparando cartas...")
        # time.sleep(1)

        if self.baralho.valor_das_cartas[carta_jogador1.valor] > self.baralho.valor_das_cartas[carta_jogador2.valor]:
            print("Jogador 1 ganha a rodada!")
            if cartas_empate:
                for carta in cartas_empate:
                    self.jogador1.inserir_carta(carta)
                cartas_empate = []
            self.jogador1.inserir_carta(carta_jogador1)
            self.jogador1.inserir_carta(carta_jogador2)

        elif self.baralho.valor_das_cartas[carta_jogador1.valor] < self.baralho.valor_das_cartas[carta_jogador2.valor]:
            print("Jogador 2 ganha a rodada!")

            if cartas_empate:
                for carta in cartas_empate:
                    self.jogador2.inserir_carta(carta)
                cartas_empate = []

            self.jogador2.inserir_carta(carta_jogador1)
            self.jogador2.inserir_carta(carta_jogador2)
        else:
            print("Empate!")
            cartas_empate.append(carta_jogador1)
            cartas_empate.append(carta_jogador2)
        print("Rodada encerrada!")

ganhadores = []

batalha = Batalha()
batalha.iniciar_batalha()
while batalha.jogador1.len_mao() > 0 and batalha.jogador2.len_mao() > 0:
    batalha.rodada()

if batalha.jogador1.len_mao() == 0 or batalha.jogador2.len_mao() == 0:
    for jogador in batalha.jogadores:
        for carta in jogador.montante:
            jogador.pontos+= batalha.baralho.valor_das_cartas[carta.valor]
        for carta in jogador.get_mao():
            jogador.pontos+= batalha.baralho.valor_das_cartas[carta.valor]
if batalha.jogador1.pontos > batalha.jogador2.pontos:
    ganhadores.append(f"{batalha.jogador1.nome} venceu! - {batalha.jogador1.pontos} pontos contra {batalha.jogador2.pontos} pontos")
elif batalha.jogador1.pontos < batalha.jogador2.pontos:
    ganhadores.append(f"{batalha.jogador2.nome} venceu! - {batalha.jogador2.pontos} pontos contra {batalha.jogador1.pontos} pontos")
else:
    ganhadores.append(f"Empate! - {batalha.jogador1.pontos} pontos contra {batalha.jogador2.pontos} pontos")
    
for ganhador in ganhadores:
    print(ganhador)

import os
import time
from baralho import Baralho
from jogador import Jogador

class Batalha():
    def __init__(self,*jogadores):
        self.jogadores = jogadores
    
    def jogar(self):
        for jogador in self.jogadores:
            jogador.mostrar_mao()

def main():
    jogadores = []

    def limpar_terminal():
        os.system("cls" if os.name == "nt" else "clear")
    limpar_terminal()

    while True:
        try:
            qntd_jogadores = int(input("Quantos jogadores? "))
            if qntd_jogadores >= 1 and qntd_jogadores <= 4:
                for i in range(qntd_jogadores):
                    nome = input(f"Digite o nome do jogador {i+1}: ")
                    jogadores.append(Jogador(nome))
            else:
                print("Apenas entre 1 e 4 jogadores")
                limpar_terminal()
                continue   
            limpar_terminal() 

        except ValueError:
            print("Digite um numero valido")

        print("Jogadores adicionados com sucesso!")
        print("Embaralhando o baralho...")
        time.sleep(1)
        baralho = Baralho()
        baralho.embaralhar()
        print("Distribuindo cartas...")
        time.sleep(1)
        baralho.distribuir_cartas(*jogadores,qtd_cartas=5)
        for jogador in jogadores:
            print(jogador)
        break
        

        
           
           
           
      

if __name__ == "__main__":
    main() 
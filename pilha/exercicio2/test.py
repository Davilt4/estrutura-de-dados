from ex2 import Pilha, PilhaException, PilhaCheiaException, PilhaVaziaException
import random
import os 

pilhas = []

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def criar_pilha():
    pilha = Pilha()
    for i in range(10):
        pilha.empilhar(random.randint(0, 9))
    pilha.local = i
    pilhas.append(pilha)

for i in range(10):
    criar_pilha()

pilha_sorteada = pilhas[random.randint(0, 9)]
pilha_sorteada.menu


while True:
    op = input("O que quer fazer: ")

    if op == "e":   
        valor = int(input("Digite o valor: "))
        pilha_sorteada.empilhar(valor)

    elif op == "d":
        try:
            valor = pilha_sorteada.desempilhar()
            print(f"Desempilhado: {valor}")
        except PilhaVaziaException:
            print("Pilha vazia")

    elif op == "t":
        print(f"Tamanho da pilha: {pilha_sorteada.tamanho}")

    elif op == "o":
        try:
            valor = pilha_sorteada.obtem_topo()
            print(f"Topo da pilha: {valor}")
        except PilhaVaziaException:
            print("Pilha vazia")

    elif op == "v":
      if pilha_sorteada.estah_vazia():
        print("Pilha vazia")
      else:
        print("Pilha nao vazia")

    elif op == "r":
        criar_pilha()
    elif op == "n":
        ...
    elif op == "z":
        ...
    elif op == "c":
        ...
    elif op == "m":
        ...
    elif op == "s":
        break

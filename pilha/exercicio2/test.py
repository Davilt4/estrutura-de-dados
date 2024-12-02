from ex2 import Pilha, PilhaException, PilhaCheiaException, PilhaVaziaException
import random
import os 

pilhas = []

 # --------------------- FUNCOES UTILITARIAS ---------------------
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def criar_pilhas(qntd,qntd_valores):
    for i in range(0,qntd):
        pilha = Pilha()
        for j in range(qntd_valores):
            pilha.empilhar(random.randint(0, 9))
        pilha.local = i
        pilhas.append(pilha)


def listar_pilhas(pilhas):
    for idx, pilha in enumerate(pilhas):
        print(f"{idx+1}: {pilha}")

#---------------------------------------------------------------------

qntd = 2
qntd_valores = 5
criar_pilhas(qntd,qntd_valores)
pilha_sorteada = pilhas[random.randint(0,qntd-1)]
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
      if pilha_sorteada.estah_vazia:
        print("Pilha vazia")
      else:
        print("Pilha nao vazia")

    elif op == "r":
        criar_pilhas()
        print("Pilha criada com sucesso")

    elif op == "n":
        print(pilha_sorteada.invertida)

    elif op == "c": #Ainda nao esta 100% funcional
        pilha1_input = int(input("Digite o indice da pilha 1: "))
        pilha2_input = int(input("Digite o indice da pilha 2: "))
        pilha1 = pilhas[pilha1_input-1]
        pilha2 = pilhas[pilha2_input-1]
           
        print("Concatenacao feita com sucesso")
        print("Pilha 1: ", pilha1)
        print("Pilha 2: ", pilha2)
        print("Pilha resultante: ", Pilha.concatenar(pilha1, pilha2) )

        
    elif op == "m":
        nova_pilha_input = input("Manualmente ou aleatoriamente? (m/a): ")
        if nova_pilha_input == "m":
            listar_pilhas(pilhas)
            pilha_input = int(input("Digite o indice da pilha: "))
            pilha_sorteada = pilhas[pilha_input-1]
            limpar_tela()
            pilha_sorteada.menu
        elif nova_pilha_input == "a":
            pilha_sorteada = pilhas[random.randint(0, 9)]
            limpar_tela()
            pilha_sorteada.menu

    elif op == "l":
        listar_pilhas(pilhas)

    elif op == "p":
        print(pilha_sorteada)

    elif op == "s":
        break

    elif op == "lt":
        limpar_tela()
        pilha_sorteada.menu
        op = input("O que quer fazer: ")


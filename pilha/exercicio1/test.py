from ex1 import Pilha, No, PilhaException, PilhaCheiaException, PilhaVaziaException


def main():
    pilha = Pilha()
   
    pilha.empilhar(1)
    pilha.empilhar(2)
    pilha.empilhar(3)
    pilha.imprimir()
    print(f"Base: {pilha.obtemBase()}")
    print(f"Subtopo: {pilha.subTopo()}")
    print("Lista esvaziada")
    pilha.esvazia()
    pilha.imprimir()
    print()
    print("Pilha com 10 elementos")
    for i in range(1,11):
        pilha.empilhar(i)
    pilha.imprimir()
    print(f"Base: {pilha.obtemBase()}")
    print(f"Subtopo: {pilha.subTopo()}")
    print()
    print("Desempilhando 5 elementos")
    pilha.desempilha_n(5)
    pilha.imprimir()
    print(f"Base: {pilha.obtemBase()}")
    print(f"Subtopo: {pilha.subTopo()}")


if __name__ == '__main__':
    main()
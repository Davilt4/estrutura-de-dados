from aula07 import *

try:
    print(conta_davi.agencia)
    print(conta_davi._conta)
    print(conta_davi.__saldo)# Não consegue ser acessado 
except AttributeError:
    print("Atributo privado nao pode ser acessado fora da classe")

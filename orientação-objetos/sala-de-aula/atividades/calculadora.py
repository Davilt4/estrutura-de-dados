import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

limpar_tela()

class Calculadora:
    def __init__(self, num1, num2, op):
        self.num1 = num1
        self.num2 = num2
        self.op = op
        self.resultado = None

    def soma(self):
        return self.num1 + self.num2

    def subtracao(self):
        return self.num1 - self.num2
    
    def multiplicacao(self):
        return self.num1 * self.num2

    def divisao(self):
        if self.num2 == 0:
            return "Erro: Divisão por zero!"
        return self.num1 / self.num2

    def __str__(self):
        return f'Operação: {self.op}, números: {self.num1} e {self.num2}, resultado: {self.resultado:.2f}' #resultado arrendado para 2 casas decimais

lista = []

nome_usuario = input("Digite seu nome: ")
primeira_execucao = True


while True:
    limpar_tela()
    if primeira_execucao:
        print(f"Olá, {nome_usuario}! Escolha a operação que deseja realizar:")
        primeira_execucao = False

    print("(+) Soma")
    print("(-) Subtração")
    print("(*) Multiplicação")
    print("(/) Divisão")

    op = input("Digite a operação (+, -, *, /): ")

    if op not in "+-*/":
        while op not in "+-*/":
            print("Operação inválida. Tente novamente.")
            op = input("Digite a operação (+, -, *, /): ")

    while True:
        try:
            num1, num2 = map(float, input("Digite os dois números separados por um espaço: ").split())
            if op == "/" and num2 == 0:
                print("Erro: Divisão por zero!")
                continue
        except ValueError:
            print("Erro: Entrada inválida! Certifique-se de digitar números corretamente.")
            continue
        break

    calc = Calculadora(num1, num2, op)

    if op == "+":
        calc.resultado = calc.soma()
    elif op == "-":
        calc.resultado = calc.subtracao()
    elif op == "*":
        calc.resultado = calc.multiplicacao()
    elif op == "/":
        calc.resultado = calc.divisao()
    else:
        print("Operação inválida. Tente novamente.")
        continue

    print(f"Resultado: {calc.resultado:.2f}") #resultado arrendado para 2 casas decimais

    lista.append(calc)

    continuar = input("Deseja realizar outra operação? (s/n): ").lower()
    if continuar == "n":
        break
  
limpar_tela()

print(f"\nHistórico de operações realizadas por {nome_usuario}:")
for item in lista:
    print(item)

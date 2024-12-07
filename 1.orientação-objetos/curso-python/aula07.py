# Modificadores de acesso (Encapsulamento)

class Conta:
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia #Atributo publico
        self._conta = conta #Atributo protected
        self.__saldo = saldo #Atributo privado, ele não é importado para fora da classe. Como visto no aula07-2

    def imprime_dados(self):
        print(f'Agência: {self.agencia} \nConta: {self._conta} \nSaldo: {self.__saldo}')

    @classmethod # Tanto faz se é classmethod ou metodo ou staticmethod
    def metodo_publico(cls):
        print('Metodo pubico')

    @staticmethod # Tanto faz se é classmethod ou metodo ou staticmethod
    def __metodo_privado():
        print('Metodo privado')

conta_davi = Conta('0001', '123456', 1000)


# print(conta_davi.agencia)
# print(conta_davi._conta)
# print(conta_davi.__saldo) # ERRO!!

Conta.metodo_publico()
# Conta.__metodo_privado() # Erro
Conta._Conta__metodo_privado() # Acessando o metodo privado (name mangling) ele muda o nome do metodo
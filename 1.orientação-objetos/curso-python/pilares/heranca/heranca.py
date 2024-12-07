# Clsse principal (Pessoa)
#  --> super class, base class, parent class
# Classe filha (Aluno)
#  --> sub class, derived class, child class


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f'{self.nome} tem {self.idade} anos.'


class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
    
    def __str__(self):
        return f'{self.nome} tem {self.idade} anos e está matriculado. classe: {self.__class__.__name__}'


class Professor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def __str__(self):
        return f'{self.nome} tem {self.idade} anos e ganha {self.salario} reais. classe: {self.__class__.__name__}'


aluno = Aluno('João', 20, 1234)
professor = Professor('Maria', 30, 5000)

print(aluno)
print(professor)
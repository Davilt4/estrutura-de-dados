class Pessoa:
    def __init__(self, nome, idade): #O primeiro atrututo é o self, que representa o objeto criado, porém pode ter qualquer nome.
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f'{self.nome} tem {self.idade} anos.'
    
    def respirar(self):
        print('Respirando...')

davi = Pessoa('Davi', 25)
print(davi)
davi.respirar()

Pessoa.respirar(davi) #Passando o objeto como parâmetro
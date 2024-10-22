import json

class Pessoa:
    ano_atual = 2024
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return (Pessoa.ano_atual - self.idade)

davi = Pessoa('Davi', 100)
print(davi.get_ano_nascimento())

print(davi.__dict__) #Retorna um dicionário com os atributos e seus valores
print(vars(davi)) #Mesma coisa

davi.__dict__["sexo"] = "M" #Adicionando um novo atributo 
print(davi.__dict__)
print(davi.sexo)
del davi.__dict__["sexo"] #Deletando um atributo
print(davi.__dict__)

lista = [davi.__dict__]

with open("orientação-objetos/json03.json", "w") as arquivo:
    json.dump(lista, arquivo,ensure_ascii=False, indent=2)
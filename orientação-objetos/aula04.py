import json

with open("orientação-objetos/json03.json", "r") as arquivo:
    dados = json.load(arquivo)

class PessoaCopia():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __str__(self):
        return f'{self.nome} tem {self.idade} anos.'

p1 = PessoaCopia(dados[0]["nome"], dados[0]["idade"]) #Criando um objeto a parit do dicionário que está no json

print(p1)
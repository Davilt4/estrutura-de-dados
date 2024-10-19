#Escopo de classe e de métodos de classe

class Animal:
   nome = "Teste"

print(Animal.nome) # TUDO CERTO

class Animal:
    def __init__(self, nome): # Agora a classe tem um construtor logo preciso criar um objeto para dar print em um atributo.
       self.nome = nome

    def comer(self,alimento):
        print(f'{self.nome} está comendo {alimento}')
    
# print(Animal.nome) Erro!!

leao = Animal('Leão')
print(leao.nome)
leao.comer('Carne')



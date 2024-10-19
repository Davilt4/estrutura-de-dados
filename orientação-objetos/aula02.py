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

class Camera:
    def __init__(self,nome,filmando = False):
        self.nome = nome
        self.filmando = filmando
    
    def ligar(self):
        self.filmando = True
        print(f'{self.nome} está Filmando')

    def desligar(self):
        self.filmando = False
        print(f'Desligando {self.nome}')

c1 = Camera('C1')
c1.ligar()
c1.desligar()        

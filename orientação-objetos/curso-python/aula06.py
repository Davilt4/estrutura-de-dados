# Getter e Property

class Caneta:
    def __init__(self, cor):
        self._cor = cor # Protected: nao pode ser acessado fora da classe
     
    @property # Getter
    def cor(self):
        print("Estou acessando o getter")
        return self._cor

    @cor.setter # Setter (Para ter um setter é necessário ter um getter)
    def cor(self, cor):
        print("Estou acessando o setter")
        self._cor = cor

    
caneta = Caneta("Azul")
caneta.cor = "Vermelha"
print(caneta.cor)
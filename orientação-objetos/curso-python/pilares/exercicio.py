class Carro:
    def __init__(self,nome,fabricante, motor):
        self.nome = nome
        self.motor = motor
        self.fabricante = fabricante
    
    def __str__(self):
        return f"{self.nome} - {self.fabricante} - {self.motor}"
    

class Motor:
    def __init__(self,nome):
        self.nome = nome
    
    def __str__(self):
        return f"{self.nome}"
    

class Fabricante:
    def __init__(self,nome):
        self.nome = nome
    
    def __str__(self):
        return f"{self.nome}"

fiat = Fabricante("Fiat")
m_fraco = Motor("Motor 1.0")
uno = Carro("Uno",fiat,m_fraco)

print(uno)
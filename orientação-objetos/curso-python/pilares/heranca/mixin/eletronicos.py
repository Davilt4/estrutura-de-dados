from log import LogPrintMixin

class Eletronico:
    def __init__(self,nome):
        self.nome = nome
        self._ligado = False
    
    def ligar(self):
        if not self._ligado:
            self._ligado = True
    
    def desligar(self):
        if self._ligado:
            self._ligado = False

class Smartphone(Eletronico,LogPrintMixin):
    def ligar(self):
        super().ligar()
        if self._ligado:
            self.logar_sucesso(f"{self.nome} está ligado")

    def desligar(self):
        super().desligar()

        
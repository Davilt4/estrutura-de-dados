import time
class Semaforo:
    def __init__(self):
        pass

    def ligar(self,tempo):
        print("Semaforo ligado")
        print()
        self.estado = "ligado"

        print("Semáforo vermelho!")
        self.cor = "vermelho"
        print(self.__dict__)
        for i in range(tempo):
            print(f"Espere {tempo-i} segundos")
            time.sleep(1)
        print()

        print("Semaforo amarelo!")
        self.cor = "amarelo"
        print(self.__dict__)
        for i in range(tempo):
            print(f"Espere {tempo-i} segundos")
            time.sleep(1)
        print()
        
        print("Semaforo verde!")
        self.cor = "verde"
        print(self.__dict__)
        for i in range(tempo):
            print(f"Espere {tempo-i} segundos")
            time.sleep(1)
        self.estado = "desligado"
        self.cor = "indefinida"

    def desligar(self,estado):
        if estado == "desligado":
            print("Semáforo já desligado")
        else:
            self.cor = "indefinida"
            self.estado = "desligado"

    def menu(self,op):
      if op == "ligar":
         return self.ligar(5)
      return self.desligar()

sm = Semaforo()

while True:
    op = input("O que quer fazer: ")
    if op == "desligar":
        break
    sm.menu(op)

print("programa encerrado")
print(sm.__dict__)
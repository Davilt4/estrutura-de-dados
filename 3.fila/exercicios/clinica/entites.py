class Cliente:
    def __init__(self,nome,cpf):
        self.__nome:str = nome
        self.__cpf:str = cpf
        self.__plano:str = None
        self._proximo: Cliente|None = None
        self._posicao_atual:int = 0

    @property
    def nome(self):
        return self.__nome
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def plano(self):
        return self.__plano

class Fila:
    def __init__(self):
        self._tamanho: int = 0
        self._primeiro: Cliente|None = None
        self._ultimo: Cliente|None = None

    def is_empty(self) -> bool:
        return self._tamanho == 0

    def adicionar(self,cliente) -> None:
        if self.is_empty():
            self._primeiro = cliente
            self._ultimo = cliente
        else:
            self._ultimo._proximo = cliente
            self._ultimo = cliente
        self._tamanho += 1
    
    def remover(self) -> Cliente:
        if self.is_empty():
            raise Exception("Fila vazia")
        cliente = self._primeiro.cliente
        self._primeiro = self._primeiro.proximo
        self._tamanho -= 1
        return cliente
    
    def posicao_atual(self,cpf) -> int:
        no = self._primeiro
        contador = 0
        while no is not None:
            contador += 1
            if no.cpf == cpf:
                return contador
            no = no._proximo
    
    def __str__(self) -> str:
        if self.is_empty():
            return "Fila vazia"
        
        clientes = ""
        no = self._primeiro
        while no is not None:
            clientes += f"{no.nome} -> "
            no = no._proximo
        return clientes
    

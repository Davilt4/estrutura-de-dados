class PilhaVaziaException(Exception):
    pass

class PilhaCheiaException(Exception):
    pass

class PilhaException(Exception):
    pass

class No:
    def __init__(self, dado: int, proximo=None):
        self.dado:int = dado
        self.proximo: No|None = proximo

    def __repr__(self):
        return f"No({self.dado})"

class Pilha:
    # solução utilizando encadeamento de objetos

    def __init__(self):
        self.__topo: No|None = None
        self.__tamanho: int = 0

    @property
    def menu(self):
        print(f'''
Editor de Pilha v1.2
=====================================
Pilha Selecionada: {self.local} de 10
[ {self.obtem_topo} ] <- topo
=====================================
(e) Empilhar
(d) Desempilhar
(t) Tamanho
(o) Obter elemento do topo
(v) Teste de pilha vazia
(r) Criar nova Pilha
(n) Inverter os elementos da pilha
(z) Esvaziar a pilha
(c) Concatenar duas pilhas
(m) Escolher outra pilha
(n) Conversão dec/bin
(s) Sair
=====================================
''')

    @property
    def estah_vazia(self) -> bool:
        return self.tamanho == 0

    @property
    def estah_cheia(self) -> bool:
        return False

    @property
    def tamanho(self) -> int:
        return self.__tamanho
    
    @property
    def obtem_topo(self) -> int:
        if self.estah_vazia:
            raise PilhaVaziaException()
        return self.__topo.dado

    def __len__(self) -> int:
        return self.tamanho

    def empilhar(self, dado: int):
        no = No(dado, proximo=self.__topo)
        self.__topo = no
        self.__tamanho += 1

    def desempilhar(self) -> int:
        if self.estah_vazia:
            raise PilhaVaziaException()
        valor = self.__topo.dado
        self.__topo = self.__topo.proximo
        self.__tamanho -= 1
        return valor
    
    # ----- Metodos da atividade ----
    def subTopo(self)->int:
        if self.estah_vazia or self.__topo.proximo is None:
            raise PilhaException()
        return self.__topo.proximo.dado
    
    def desempilha_n(self, n: int) -> bool:
        if self.estah_vazia or n > self.__tamanho:
            return False
        for i in range(n):
            self.desempilhar()
        return True
    
    def esvazia(self):
        if not self.estah_vazia:
            while not self.estah_vazia:
                self.desempilhar()
        PilhaVaziaException()

    def obtemBase(self)->int:
        if self.estah_vazia:
            raise PilhaVaziaException
        base = self.__topo
        while base.proximo is not None:
            base = base.proximo
        return base.dado
        

    def __str__(self) -> str:
        resposta = "["
        no_atual: No|None = self.__topo
        for x in range(self.tamanho):
            resposta += str(no_atual.dado)
            if x != self.tamanho - 1:
                resposta += ", "
            no_atual = no_atual.proximo
        resposta += "]"
        return resposta
    
    def imprimir(self):
        print(self)

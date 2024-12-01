class Node:
    def __init__(self, value):
        self.value = value
        self.next = None #Referencia para o proximo no

class LinkedStack:
    def __init__(self):
        self.head = None # Topo da pilha

    @property
    def is_empty(self):
        return self.head is None
    
    @property
    def peek(self):
        if self.is_empty:
            raise IndexError("A pilha está vazia")
        return self.head.value
    
    def push(self,value):
        new_node = Node(value)
        new_node.next = self.head 
        self.head = new_node
    

    def pop(self):
        if self.is_empty:
            raise IndexError("A pilha está vazia")
        element = self.head.value
        self.head = self.head.next
        return element
    
    def __str__(self):
        elements = ""
        element = self.head
        while element:
            if element.next is not None:
                elements += str(f"{element.value} -> ")
            else:
                elements += str(f"{element.value}")
            element = element.next
        return elements


# Na primeira instancia do No, o seu self.next ira Ser None pois o head da pilha começa como None. E o topo da pilha sera o No instanciado.

# Na segunda instacia do No, a pilha ja tem um valor de Head, entao o seu self.next ira ser esse Head.

'''Exemplo: No(6); no.next = None
            pilha.head = No(6)

            No(7); no.next = Pilha.head(No(6))
            pilha.head = No(7)
'''

def main():
    stack = LinkedStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)

    stack.pop()
    print(stack)

    head = stack.head.value
    peek = stack.peek
    print(head)
    print(peek)

if __name__ == "__main__":
    main()    
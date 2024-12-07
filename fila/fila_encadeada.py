class EmptyQueueError(Exception):
    def __init__(self):
        super().__init__("Empty Queue!")

class Node:
    def __init__(self,value):
        self.value: int = value
        self.next: Node|None = None

class Queue:
    def __init__(self):
        self._size = 0
        self.last: Node|None = None
        self.frist: Node|None = None
    
    @property
    def is_empty(self) -> bool:
        return self._size == 0
    
    @property
    def info(self):
        return f"frist element: {self.frist.value}\nlast element: {self.last.value}\nsize: {self._size}\n"

    def push(self,value):
        node = Node(value)
        if self.is_empty:
            self.frist = node
            self.last = node
        elif self._size == 1:
            self.frist.next = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self._size+=1

    def pop(self) -> int:
        value = self.frist.value
        self.frist = self.frist.next
        self._size -= 1
        return value
    
    def __str__(self):
        queue = ""
        element = self.frist
        while element != None:
            if element.next is None:
                queue += f"{element.value}"
            else:
                queue += f"{element.value} -> "
            element = element.next
        return queue
    
    

queue = Queue()

queue.push(1)
queue.push(2)
queue.push(3)
print(queue)
print(queue.info)

queue.push(4)
print(queue)
print(queue.info)

queue.pop()
print(queue)
print(queue.info)
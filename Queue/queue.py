######### Implement queue using array #########
class queueUsingArray:
    def __init__(self, size):
        self._size = size
        self._array = [None]* self._size
        self._rear = -1
        self._front = -1
    def isFull(self):
        return (self._rear +1)%self._size == self._front
    def isEmpty(self):
        return self._front == self._rear == -1
    def front(self):
        if not self.isEmpty():
            return self._array[self._front]
        raise ValueError('Queue is empty')
    def enQueue(self, data):
        if self.isEmpty():
            self._rear = 0
            self._front = 0
        else:
            if self.isFull():
                raise Exception('Queue is full')
            self._rear = (self._rear + 1)% self._size
        self._array[self._rear] = data
    def deQueue(self):
        if self.isEmpty():
            raise Exception('Queue is empty')
        elif self._rear == self._front:
            data = self.front()
            self._rear = self._front = -1
        else:
            data = self.front()
            self._front = (self._front + 1)% self._size
        return data


# queue = queueUsingArray(5)
# print(queue.isEmpty())
# queue.enQueue(1)
# queue.enQueue(2)
# queue.enQueue(3)
# queue.enQueue(4)
# queue.enQueue(5)
# print(queue.front())
# print(queue.deQueue())
# print(queue.deQueue())
# print(queue.deQueue())
# print(queue.deQueue())
# print(queue.deQueue())

######### Implement queue using linked list #########
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class queueUsingLinkedList:
    def __init__(self):
        self.head = None
        self._rear = None
        self._size = 0
    def front(self):
        return self.head.data
    def isEmpty(self):
        return self._size == 0
    def deQueue(self):
        if self.isEmpty():
            raise ValueError('Queue is empty')
        elif self._size == 1:
            data = self.front()
            self.head = self._rear =None
            self._size -=1
        else:
            temp = self.head.next
            data = self.front()
            self.head.data = self.head.next.data
            self. head.next = self.head.next.next
            del temp
            self._size -=1
        print(f'Pop: {data}')
        return data
    def enQueue(self, data):
        Node = node(data)
        if self.isEmpty():
            self.head = Node
            self._rear = Node
            self._size +=1
            return
        self._size +=1
        self._rear.next = Node
        self._rear = self._rear.next


queue = queueUsingLinkedList()
queue.enQueue(1)
queue.enQueue(2)
queue.enQueue(3)
queue.enQueue(4)
queue.enQueue(5)
# print(queue.front())
queue.deQueue()
queue.deQueue()
queue.deQueue()
queue.deQueue()
queue.deQueue()
# queue.deQueue()
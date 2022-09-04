######### Implement stack using linked list #########
class node:
    def __init__(self, data):
        self.data = data 
        self.next = None


class stack: 
    def __init__(self):
        self.head = None
        self.size = 0
    def isEmpty(self):
        return self.size == 0
    def push(self, data):
        Node = node(data)
        Node.next = self.head
        self.head = Node
        self.size +=1 
    def pop(self):
        if self.isEmpty(): 
            raise Exception('The stack is empty, can not perform this operation.')
        data = self.head.data
        self.head.data = self.head.next.data
        temp = self.head.next
        self.head.next = self.head.next.next
        del temp
        self.size-=1
        print(f'Pop: {data}')
        return data

class Stack:
    def __init__(self):
        self.array = []
        self.top = -1
    def isEmpty(self):
        return self.top == -1
    def push(self, data):
        self.array.append(data)
        self.top += 1
    def remove(self):
        self.array.pop()
        self.top -= 1
    def peek(self):
        if self.isEmpty():
            raise Exception('The stack is empty')
        return self.array[self.top]


def printNode(head):
    while head:
        print(head.data)
        head = head.next


st = stack()
# print(st.isEmpty())
st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.push(5)
st.pop()
printNode(st.head)
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
        if self.size == 1:
            self.head = None
        else:
            self.head.data = self.head.next.data
            temp = self.head.next
            self.head.next = self.head.next.next
            del temp
        self.size-=1
        print(f'Pop: {data}')
        return data


def printNode(head):
    while head:
        print(head.data)
        head = head.next

######### Implement stack using array #########
class Stack:
    def __init__(self):
        self.array = []
        self.top = -1
        self._max = []
        self._min = []
    def isEmpty(self):
        return self.top == -1
    def maxStack(self, data):
        if self.isEmpty():
            self._max.append(data)
        elif self._max[self.top] < data:
            self._max.append(data)
        else: self._max.append(self._max[self.top])
    def minStack(self, data):
        if self.isEmpty():
            self._min.append(data)
        elif self._min[self.top] > data:
            self._min.append(data)
        else: self._min.append(self._min[self.top])
    def getMax(self):
        return self._max[self.top]
    def getMin(self):
        return self._min[self.top]
    def push(self, data):
        self.array.append(data)
        self.maxStack(data)
        self.minStack(data)
        self.top += 1
    def remove(self):
        self._max.pop()
        self._min.pop()
        self.top -= 1
        return self.array.pop()
    def peek(self):
        if self.isEmpty():
            raise Exception('The stack is empty')
        return self.array[self.top]




st = stack()
print(st.isEmpty())
st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.push(5)
st.pop()
st.pop()
st.pop()
st.pop()
st.pop()
printNode(st.head)

# stac = Stack()
# stac.push(1)
# stac.push(2)
# stac.push(3)
# stac.push(4)
# stac.push(5)
# stac.push(6)
# stac.remove()
# print(stac.getMax())
# print(stac.getMin())
# for i in stac.array:
#     print(i)
class linkedList: 
    def __init__(self, data = None):
        self.data = data
        self.next = None


def printLinkedList(self): # only for head Node 
    iteratedVariable = self
    while iteratedVariable:
        print(iteratedVariable.data)
        iteratedVariable = iteratedVariable.next


def mergeTwoLinkedList(l1, l2):
    dummy = tail = linkedList()
    while l1 and l2: 
        if l1.data <= l2.data:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next
    tail.next = l1 or l2 
    return  dummy.next



#------Creating linked lists------#
l1 = linkedList(5)
l1.next = linkedList(10)
l1.next.next = linkedList(15)
l1.next.next.next = linkedList(20)
l1.next.next.next.next = linkedList(25)

l2 = linkedList(1)
l2.next = linkedList(6)
l2.next.next = linkedList(11)
l2.next.next.next = linkedList(16)
l2.next.next.next.next = linkedList(21)

#-------------Merging-------------#
l3 = mergeTwoLinkedList(l1, l2)


#------Printing linked lists------#
printLinkedList(l3)

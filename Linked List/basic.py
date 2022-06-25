class node: 


    def __init__(self, data):
        self.data = data
        self.next = None


    def deleteANodeAfter(self): # not apply for the tail
        self.next = self.next.next


    def insertANodeAfter(self, Node):
        Node.next = self.next
        self.next = Node


class linkedList: 


    def __init__(self):
        self.head = None


    def printLinkedList(self):
        iterateThroughLL = self.head
        while iterateThroughLL:
            print(iterateThroughLL.data)
            iterateThroughLL = iterateThroughLL.next


    def search(self, number): # search if a data is available
        iterateThroughLL = self.head
        while iterateThroughLL:
            if iterateThroughLL.data == number:
                print('{number} is existed'.format(number = number))
                return
            iterateThroughLL = iterateThroughLL.next
        print('{number} is not existed'.format(number = number))


#------Creating linked lists------#
#--Add value--#
element = linkedList()
element.head = node(0)
element1 = node(1)
element2 = node(2)
element3 = node(3)
element4 = node(2.5)


#--Add links--#
element.head.next = element1
element1.next = element2
element2.next = element3

#------Linked list operations------#
# element1.deleteANodeAfter()
element.search(3)
element3.insertANodeAfter(element4)



#------Print the linked list------#
element.printLinkedList()




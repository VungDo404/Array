from node import *

def removeDuplicate(head):
    while head.next:
        if head.data == head.next.data:
            deleteNode(head)
            continue
        head = head.next



#--------------------#
head = node(0)
head.next = node(0)
head.next.next = node(0)
head.next.next.next = node(2)
head.next.next.next.next = node(3)
head.next.next.next.next.next = node(3)
head.next.next.next.next.next.next = node(3)
head.next.next.next.next.next.next.next = node(5)


#-------------------#
removeDuplicate(head)
head.printNode()
from tkinter import N


class node:
    def __init__(self, data = None): 
        self.data = data
        self.next = None


def printList(self):
    iterateVariable = self
    while iterateVariable:
        print(iterateVariable.data)
        iterateVariable = iterateVariable.next


def reverseList1(head):
    prev = None
    while head:
        track, head.next = head.next, prev
        prev, head  = head, track 
    return prev


def reverseList2(head):
    if head is None:
        return head 
    newHead = head
    while head.next:
        newHead = reverseList2(head.next)
        head.next.next = head
        head.next = None
    return newHead


def reverseList3(head, start, finish): # assume that start and finish are in length of the lists
    LP= dummy = node()
    dummy.next = head
    count = 1
    while count < start:
        count += 1
        LP, head = head, head.next
    prev = None
    for i in range(start, finish+1):
        carry, head.next = head.next, prev
        prev, head = head, carry
    LP.next.next = head
    LP.next = prev
    return dummy.next

#------Creating linked lists------#
l1 = node(1)
l1.next = node(2)
l1.next.next = node(3)
l1.next.next.next = node(4)

#------Reverse------#
rev = reverseList3(l1, 2, 4)

#------Print------#
printList(rev)


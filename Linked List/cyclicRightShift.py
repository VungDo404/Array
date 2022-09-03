from node import * 

def getLength(head):
    length = 0
    while head: 
        length+=1
        head=head.next
    return length

# abc shift 2 --> bca, shift 1 --> cab
def cyclicRightShift(head, shift):
    length = getLength(head)
    shift %= length
    if shift == 0:
        return head
    step = length - shift -1 
    tail, temp = head, head
    while step != 0:
        temp = temp.next
        step-=1 
    while tail.next:
        tail = tail.next
    tail.next = head
    newHead, temp.next  = temp.next, None
    return newHead


#--------------------#
head = node(0)
head.next = node(1)
head.next.next = node(2)
head.next.next.next = node(3)
head.next.next.next.next = node(4)
head.next.next.next.next.next = node(5)
head.next.next.next.next.next.next = node(6)
head.next.next.next.next.next.next.next = node(7)

#---------------------#
head = cyclicRightShift(head, 8)
head.printNode()
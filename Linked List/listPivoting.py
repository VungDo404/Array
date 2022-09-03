from node import *

def listPivoting(head, k):
    headLess = indexLess = node(0)
    headEqua = indexEqua = node(0)
    headGreater = indexGreater = node(0)
    while head:
        if head.data < k:
            indexLess.next = head
            indexLess = indexLess.next
        elif head.data == k:
            indexEqua.next = head 
            indexEqua = indexEqua.next
        else: 
            indexGreater.next = head
            indexGreater = indexGreater.next
        head = head.next 
    indexGreater.next = None
    indexEqua.next = headGreater.next
    indexLess.next = headEqua.next
    return headLess.next


#----------------------#
head = node(3)
head.next = node(2)
head.next.next = node(2)
head.next.next.next = node(11)
head.next.next.next.next = node(7)
head.next.next.next.next.next = node(5)
head.next.next.next.next.next.next = node(11)
head.next.next.next.next.next.next.next = node(12)

# tempHead = temp = node(None)
# temp.next = head.next
# temp = temp.next 
# temp.next = head.next.next.next
# temp = temp.next 
# temp.next = head.next.next.next.next.next.next
# temp = temp.next
# temp.next = None 
#----------------------#
head = listPivoting(head,7)
head.printNode()
# tempHead.next.printNode()
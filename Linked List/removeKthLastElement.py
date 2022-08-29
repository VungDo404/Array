from node import * 

def deleteKthLastElement(head, kth):
    if kth==1: 
        deleteLastNode(head)
        return
    left,right = head, head
    while kth != 0: 
        right = right.next
        kth-=1
    while right:
        right, left = right.next, left.next
    deleteNode(left)


#-----------------------#
head = node(1)
head.next = node(2)
head.next.next = node(3)
head.next.next.next = node(4)

print('Original list:')
head.printNode()
#------------------#
print('Modified list') 
deleteKthLastElement(head,4)
head.printNode()
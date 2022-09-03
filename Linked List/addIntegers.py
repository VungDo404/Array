from node import * 

def adder(l1, l2): 
    head =l3 = node(0)
    carry = 0 
    while l1 or l2 or carry: 
        sum = (l1.data if l1 else 0) + (l2.data if l2 else 0) + carry
        carry =  sum//10
        l3.next  = node(sum %10)
        l3 = l3.next
        l1, l2 = (l1.next if l1 else None), (l2.next if l2 else None)
    return head.next

#---------------------------#
l1 = node(2)
l1.next = node(4)
l1.next.next = node(3)

l2 = node(5)
l2.next = node(6)
l2.next.next = node(9)
l2.next.next.next = node(9)
#---------------------------#
l3 = adder(l1,l2)
l3.printNode()
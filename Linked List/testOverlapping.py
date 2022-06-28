class node:
    def __init__(self, data):
        self.data = data
        self.next = None


def isOverlap(l1, l2):
    length1 =0
    length2 =0
    head1, head2 = l1, l2
    while head1:
        length1 +=1
        head1 = head1.next    
    while head2:
        length2 +=1
        head2 = head2.next
    diff = length2 - length1
    if(diff >=0):
        for i in range(diff):
            l2 = l2.next
        while l1 and l2 and l1 != l2:
            l1 = l1.next
            l2 = l2.next
        return l1
    for i in range(diff):
        l1 = l1.next
        while l1 and l2 and l1 != l2:
            l1 = l1.next
            l2 = l2.next
        return l1

#--------------------------#
element = node(0)
element.next = node(1)
element.next.next = node(2)
element.next.next.next = node(3)
element.next.next.next.next = node(4)
element.next.next.next.next.next = node(5)

element1 = node(10)
element1.next = node(11)
element1.next.next = node(12)
element1.next.next.next = node(14)
# element1.next.next.next.next = node(14)
# element1.next.next.next.next.next = node(15)
#--------------------------#
if(isOverlap(element1, element)):
    print(True)
else: print(False)
class ListNode:


    def __init__(self, x):
            self.val = x
            self.next = None
    def printList(self):
        iterateVariable = self
        while iterateVariable:
            print(iterateVariable.val)
            iterateVariable = iterateVariable.next


l = ListNode(1)
l.next = ListNode(4)
l.next.next = ListNode(5)

r = ListNode(1)
r.next = ListNode(3)
r.next.next = ListNode(4)


dummy = cur = ListNode(0)

# dummy.next = l
# dummy.printList()
# print("-----Cur-----")
# cur = cur.next
# cur.next = r
# cur.printList()
# print("-----Dummy-----")
# dummy.printList()
# print("----------")
# l.printList()

for i in range(0,5):
    print('Outside (1) while loop',i)
    while i >= 3 and i <= 7:
        print('Inside while loop',i)
        i += 0.5
    print('Outside (2) while loop',i)
    
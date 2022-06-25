# Floyd's Tortoise and Hare 
class node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def checkCyclicity(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False


#---------------------#
element = node(0)
element.next = node(1)
element.next.next = node(2)
element.next.next = node(3)
element.next.next = element.next

element1 = node(10)
element1.next = node(11)
element1.next.next = node(12)
element1.next.next.next = node(13)
element1.next.next.next.next = node(14)
#---------------------#
print(element.checkCyclicity(element))
print(element1.checkCyclicity(element1))
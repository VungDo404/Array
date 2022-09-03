from node import *

def reverseLinkedList(head):
    dummy = None
    while head:
        next, head.next = head.next, dummy
        dummy, head  = head, next
    return dummy

def isPalindrome(head):
    left, right = head, head
    while right.next and right.next.next:
        right, left = right.next.next, left.next
    left = left.next
    left = reverseLinkedList(left)
    while left and head.data == left.data:
        head, left = head.next, left.next
    return not left

#--------------------#
head = node(1)
head.next = node(2)
head.next.next = node('p')
head.next.next.next = node(3)
head.next.next.next.next = node(1)

h = node(5)
h.next = node(2)
h.next.next = node(2)
h.next.next.next = node(5)

#--------------------#
print(isPalindrome(h))

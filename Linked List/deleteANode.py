from node import *


def deleteNode(node):
    node.data = node.next.data
    node.next = node.next.next 

#------------------# 
head = node(1)
head.next = node(2)
head.next.next = node(3)
head.next.next.next = node(4)

print('Original list:')
head.printNode()
#------------------#
print('Modified list') 
deleteNode(head.next)
head.printNode()

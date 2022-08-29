class node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def printNode(head):
        while head:
            print(head.data)
            head = head.next



def deleteNode(this):
    this.data = this.next.data
    this.next = this.next.next 
def deleteLastNode(head):
    while head.next.next: 
        head = head.next
    head.next = None
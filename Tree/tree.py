class node:
    def __init__(self, data= None):
        self.data = data
        self.left = None
        self.right = None
    def insert(self,data): # BST
        if self.data is None:
            self.data = data
        elif data <= self.data:
            if self.left is None:
                self.left =node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = node(data)
            else: 
                self.right.insert(data) 
    def inOrder(self):
        if self.left:
            self.left.inOrder()
        print(self.data)
        if self.right:
            self.right.inOrder()
    def find(self, value):
        if self.data == value:
            return True
        elif value < self.data:
            return self.left.find(value) if self.left else False
        return self.right.find(value) if self.right else False


# root = node(10)
# root.insert(9)
# root.insert(11)
# root.insert(8)
# root.insert(12)
# root.inOrder()
# print(root.find(13))

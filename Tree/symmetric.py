from tree import *

def checkSymmetric(nodeLeft, nodeRight):
    if not (nodeLeft and nodeRight):
        return True
    elif nodeLeft and nodeRight:
        return nodeLeft.data == nodeRight.data and checkSymmetric(nodeLeft.left, nodeRight.right) and checkSymmetric(nodeLeft.right, nodeRight.left)
    return False
def isSymmetric(root):
    return checkSymmetric(root.left, root.right) or not root



root = node(314)
root.left = node(6)
root.right = node(6)
root.left.right = node(2)
root.right.left = node(2)
root.left.right.right = node(3)
root.right.left.left = node(1)
print(isSymmetric(root))

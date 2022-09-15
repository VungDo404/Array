from tree import *

def isBalanced(root):
    if root is None:
        return [True, 0]
    left, right = isBalanced(root.left), isBalanced(root.right)
    height = abs(left[1]-right[1])
    balanced = left[0] and right[0] and height <= 1
    return [balanced, max(left[1], right[1])+1]

def length(root):
        if not root: 
            return 0,True
        left = length(root.left)
        right = length(root.right)
        balanced = left[0] and right[0] and abs(left[0]-right[0]) <= 1
        return max(left[0],right[0])+1, balanced


root = node(3)
# root.left = node(9)
# root.right = node(20)
# root.right.left =node(15)
# root.right.right= node(7)
# root.inOrder()
print(isBalanced(root)[0])
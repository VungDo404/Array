from tree import *


def dfs(root,k):
    k-=1
    stack = []
    stack.append(root)
    n=0
    node =root
    while stack: 
        if stack[-1].left and node:
            stack.append(stack[-1].left)
        else:
            node = stack.pop()
            if k == n: return node.data
            n+=1
            if node.right:
                stack.append(node.right)
            else:
                node = None

root = node(10)
root.insert(1)
root.insert(0)
root.insert(2.5)
root.insert(2)
root.insert(3)
root.insert(4)
root.insert(5)
root.insert(6)
root.insert(7)
root.insert(8)
root.insert(11)
root.insert(12)
root.insert(13)
root.insert(15)
root.insert(16)
root.insert(17)
root.insert(18)
root.insert(21)
print(dfs(root,19))
def simplify(path):
    stack = []
    cur = ""
    for c in path :
        if c == "/":
            if cur == ".." and stack:
                stack.pop()
            elif cur != "" and cur !=".":
                stack.append(cur)
            cur = ''
        else: 
            cur += c
    return '/' + '/'.join(stack)

path =  '/home/'
print(simplify(path))


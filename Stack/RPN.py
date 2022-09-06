token = ['2', '2']
res = 0
convert = {}
# if token[2] == '/':
#     res = int(token[1]) / int(token[0])
# s = 'hello world' if  not int('*') else True

def RPN(token):
    stack = []
    for c in token:
        if c == '+':
            value = stack.pop() + stack.pop()
            stack.append(value)
        elif c == '-':
            value = -stack.pop() + stack.pop()
            stack.append(value)
        elif c == '*':
            value = stack.pop() * stack.pop()
            stack.append(value)
        elif c == '/':
            value = int(1/(stack.pop() / stack.pop()))
            stack.append(value)
        else: 
            stack.append(int(c))
    return stack[-1]


tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(RPN(tokens))
def toInt(string):
    integer = 0
    if len(string) == 1:
        integer = ord(string[0]) -48
        return integer
    for i in range(len(string)): 
        integer += toInt(string[i]) * pow(10,len(string)-1-i)
    return integer


integer = toInt('12342342')
# print('Type of',integer,'is',type(integer))


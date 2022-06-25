def baseConversion(number, originBase, convertedBase):
    total = 0
    number = number[::-1]
    A = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    for i in range(len(number)):
        total += int(number[i]) * pow(originBase,i)
    output = ''
    while total != 0:
        res = total % convertedBase
        output += A[res]
        total //= convertedBase
    output = output[::-1]
    return output


converted = baseConversion('615', 7, 13)
print(converted)


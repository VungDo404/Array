def mutiply(num1, num2):
    len1 = len(num1)
    len2 = len(num2)
    result = [0] * (len1 + len2)
    num1, num2 = num1[::-1], num2[::-1] # reverse num1 and num2
    for i in range(len1) :
        for j in range(len2): 
            digits = int(num1[i]) * int(num2[j]) 
            result[i+j] += digits
            result[i+j+1] += result[j+i] // 10
            result[i+j] = result[j+i] % 10
    result, zero = result[::-1], 0
    while zero < len1+len2 and result[zero] == 0:
        zero += 1
    result = map(str, result[zero::]) 
    readableResult = ''.join(result)
    return readableResult


#------------------------#
result = mutiply('123','543')
print(result)
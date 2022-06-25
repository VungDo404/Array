def prime(n):
    ifPrime = [False, False] + [True]*(n-1)
    for i in range(2,n+1):
        m = 2
        while i*m <= n:
            ifPrime[i*m] = False
            m += 1
    result = []
    for i in range(len(ifPrime)):
        if ifPrime[i] == True:
            result.append(i)
    return result


n = prime(10)
print(n)
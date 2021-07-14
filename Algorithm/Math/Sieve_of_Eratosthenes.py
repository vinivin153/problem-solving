def isPrime(n):
    s = [True for _ in range(n + 1)]
    m = int(n ** 0.5) + 1
    for i in range(2, m + 1):
        if s[i] == True:
            for j in range(i + i, n + 1, i):
                s[j] = False
    for i in range(2, n + 1):
        if s[i] == True:
            print(i)


# solution2
"""
for i in range(2, MAX+1):
    if isPrime[i]:
        prime.append(i)
        j = i
        while i*j <= MAX:
            isPrime[i*j] = False
            j += 1
"""

isPrime(120)

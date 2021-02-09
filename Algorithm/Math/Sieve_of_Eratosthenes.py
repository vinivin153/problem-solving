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


isPrime(120)

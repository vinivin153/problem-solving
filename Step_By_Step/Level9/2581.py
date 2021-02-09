def isPrime(m, n):
    if n == 1:
        return
    s = [True for _ in range(n + 1)]
    s[1] = False
    t = int(n ** 0.5) + 1
    for i in range(2, t + 1):
        if s[i] == True:
            for i in range(i + i, n + 1, i):
                s[i] = False
    return [i for i in range(m, n + 1) if s[i] == True]


a = isPrime(int(input()), int(input()))
if not a:
    print(-1)
else:
    print(sum(a), min(a), sep="\n")

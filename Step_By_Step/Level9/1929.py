def pNumber(m: int, n: int):
    s = int(n ** 0.5) + 1
    a = [0 for _ in range(n + 1)]
    a[1] = 1
    for i in range(2, s + 1):
        if a[i] == 0:
            for j in range(i + i, n + 1, i):
                a[j] = 1
    for i in range(m, n + 1):
        if a[i] == 0:
            print(i)


m, n = map(int, input().split())
pNumber(m, n)

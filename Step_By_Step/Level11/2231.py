def constuctor(n: int):
    k = 1
    sumNumber = 0
    while k <= n:
        sumNumber += (n // k) % 10
        k *= 10
    return sumNumber + n


n = int(input())
if n < 54:
    for i in range(n):
        if constuctor(i) == n:
            print(i)
            break
    else:
        print(0)
else:
    for i in range(n - 54, n):
        if constuctor(i) == n:
            print(i)
            break
    else:
        print(0)

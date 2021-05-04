n = list(map(int, input().split()))

while True:
    for i in range(4):
        if n[i] > n[i + 1]:
            n[i], n[i + 1] = n[i + 1], n[i]
            print(*n)
    if [1, 2, 3, 4, 5] == n:
        break

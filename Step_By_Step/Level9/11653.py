n = int(input())
m = int(n ** 0.5) + 1
d = 2
while d <= m and n != 1:
    if n % d == 0:
        print(d)
        n //= d
    else:
        d += 1
if n != 1:
    print(n)
n = 1
a = [0 for i in range(10001)]
while True:
    num = n + n % 10 + (n // 10) % 10 + (n // 100) % 10 + n // 1000
    if n > 10000:
        break
    else:
        if num <= 10000:
            a[num] += 1
        n += 1

for i in range(1, 10001):
    if a[i] == 0:
        print(i)
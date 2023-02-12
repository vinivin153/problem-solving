n, k = map(int, input().split())
s = list(map(int, input().split()))

ss = []
for i in range(n - 1):
    ss.append(s[i + 1] - s[i])

ss.sort()
print(sum(ss[: n - k]))

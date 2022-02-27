import sys

input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))
seq.insert(0, 0)

dp1 = [1 for _ in range(n + 1)]
dp2 = [[] for _ in range(n + 1)]
dp1[0] = 0
for i in range(1, n + 1):
    dp2[i].append(seq[i])


for i in range(2, n + 1):
    max_val = 0
    idx = 0
    for j in range(1, i):
        if seq[i] > seq[j] and max_val < dp1[j]:
            max_val = dp1[j]
            idx = j
    dp1[i] += max_val
    dp2[i] = dp2[idx] + dp2[i]

a = dp1.index(max(dp1[1:]))
print(dp1[a])
print(*dp2[a])

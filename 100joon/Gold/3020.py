import sys

input = sys.stdin.readline
n, h = map(int, input().split())
floor = [0] * (h + 1)
ceiling = [0] * (h + 1)

for i in range(n):
    if i % 2:
        floor[int(input())] += 1
    else:
        ceiling[int(input())] += 1


for i in range(h - 1, 0, -1):
    floor[i] += floor[i + 1]
    ceiling[i] += ceiling[i + 1]

prefixSum = [0] * (h + 1)
prefixSum[0] = 10**9
for i in range(1, h + 1):
    prefixSum[i] = floor[i] + ceiling[h + 1 - i]


min_value = min(prefixSum)
print(min_value, prefixSum.count(min_value))

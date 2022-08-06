import sys


input = sys.stdin.readline
n, k = map(int, input().split())
temp = list(map(int, input().split()))

max_temp = sum(temp[:k])
val = max_temp
for i in range(1, n - k + 1):
    val = val - temp[i - 1] + temp[i + k - 1]
    max_temp = max(max_temp, val)

print(max_temp)

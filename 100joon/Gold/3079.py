import sys

input = sys.stdin.readline
n, m = map(int, input().split())
tables = []
for _ in range(n):
    tables.append(int(input()))

left = 1
right = max(tables) * m
ans = -1
while left <= right:
    mid = (left + right) // 2
    total = 0
    for table in tables:
        total += mid // table

    if total >= m:
        ans = mid
        right = mid - 1
    elif total < m:
        left = mid + 1

print(ans)

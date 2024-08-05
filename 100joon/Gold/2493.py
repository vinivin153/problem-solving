import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

ans = [0] * n
stack = []
stack.append((n - 1, arr[-1]))
for i in range(n - 2, -1, -1):
    while stack and stack[-1][1] <= arr[i]:
        idx, _ = stack.pop()
        ans[idx] = i + 1
    stack.append((i, arr[i]))

print(*ans)

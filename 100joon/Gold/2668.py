import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
nums = defaultdict()

for i in range(1, n + 1):
    j = int(input())
    nums[i] = j

ans = set()
visited = [0] * (n + 1)


def dfs(start):
    stack = []
    history = [0]
    stack.append(start)
    idx = 1
    while stack:
        x = stack.pop()
        if visited[x]:
            if x in history:
                ans.update(history[visited[x] :])
            break
        visited[x] = idx
        history.append(x)
        stack.append(nums[x])
        idx += 1


for i, v in nums.items():
    if not visited[i]:
        dfs(i)

print(len(ans))
for item in sorted(ans):
    print(item)

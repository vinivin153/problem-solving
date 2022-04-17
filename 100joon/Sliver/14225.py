import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

res = {0}
visited = [0] * n


def backtracking(val, idx):
    if val not in res:
        res.add(val)

    for i in range(idx, n):
        if visited[i] == 0:
            visited[i] = 1
            backtracking(val + nums[i], i)
            visited[i] = 0


backtracking(0, 0)

i = 1
while True:
    if i not in res:
        print(i)
        break
    i += 1

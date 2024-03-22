import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
seq = list(map(int, input().split()))
parent = [i for i in range(n)]


visited = set()


def dfs(x):
    stack = [x]
    visited.add(x)
    while stack:
        s = stack.pop()
        for idx, isConnected in enumerate(mat[s]):
            if idx != s:
                if isConnected and idx not in visited:
                    visited.add(idx)
                    stack.append(idx)


dfs(seq[0] - 1)

for i in seq:
    if i - 1 not in visited:
        print("NO")
        break
else:
    print("YES")

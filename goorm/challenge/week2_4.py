# 폭탄 구현하기
import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
mat = [[0 for _ in range(n)] for _ in range(n)]

queue = deque()
for _ in range(k):
    s, e = map(int, input().split())
    queue.append([s - 1, e - 1])

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
while queue:
    x, y = queue.popleft()
    mat[x][y] += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            mat[nx][ny] += 1
ans = 0
for i in mat:
    ans += sum(i)
print(ans)

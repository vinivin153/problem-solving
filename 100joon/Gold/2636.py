import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
mat = []

cnt = 0
for _ in range(n):
    k = list(map(int, input().split()))
    cnt += k.count(1)
    mat.append(k)


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def find_c(kk):
    global cnt
    queue = deque()
    queue.append((kk, kk))
    flag = 0
    visited = set()
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 + kk <= nx < n - kk
                and 0 + kk <= ny < m - kk
                and (nx, ny) not in visited
            ):
                if mat[nx][ny] == 1:
                    mat[nx][ny] = 0
                    cnt -= 1
                    flag = 1
                else:
                    queue.append((nx, ny))
                visited.add((nx, ny))


k = 0
res = [cnt]
while cnt:
    find_c(k)
    k += 1
    res.append(cnt)

print(k)
print(res[-2])

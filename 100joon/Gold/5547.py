import sys
from collections import deque

input = sys.stdin.readline
m, n = map(int, input().split())

mat = [[0 for _ in range(m + 2)]]
for _ in range(n):
    mat.append([0] + list(map(int, input().split())) + [0])
mat.append([0 for _ in range(m + 2)])


dx = [-1, -1, 0, 0, 1, 1]
dy1 = [0, 1, -1, 1, 0, 1]
dy2 = [-1, 0, -1, 1, -1, 0]


def is_valid_scope(nx, ny):
    if 0 <= nx <= n + 1 and 0 <= ny <= m + 1:
        return True
    else:
        return False


answer = 0


def find_outside():
    global answer
    mat[0][0] = -1
    queue = deque()
    queue.append((0, 0))
    while queue:
        x, y = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y
            if x % 2 == 1:
                ny = y + dy1[i]
            else:
                ny = y + dy2[i]
            if is_valid_scope(nx, ny):
                if mat[nx][ny] == 0:
                    mat[nx][ny] = -1
                    queue.append((nx, ny))
                elif mat[nx][ny] == 1:
                    answer += 1


find_outside()
print(answer)

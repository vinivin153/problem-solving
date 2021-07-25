from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    cnt = 0
    while queue:
        x, y = queue.popleft()
        visited[(x, y)] = 1
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and (nx, ny) and 0 <= ny < n:
                if (
                    apart[nx][ny] == 1
                    and (nx, ny) not in visited
                    and (nx, ny) not in queue
                ):
                    queue.append((nx, ny))
    return cnt


n = int(input())
apart = [list(map(int, input())) for i in range(n)]

visited = {}
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

apart_complex = 0
apart_cnt = []
for i in range(n):
    for j in range(n):
        if apart[i][j] == 1 and (i, j) not in visited:
            apart_complex += 1
            apart_cnt.append(bfs(i, j))

apart_cnt.sort()
print(apart_complex)
for i in apart_cnt:
    print(i)

from collections import deque

s = int(input())


def bfs():
    queue = deque()
    queue.append((1, 0))
    visited[1][0] = 0
    while queue:
        x, cb = queue.popleft()
        if x == s:
            print(visited[x][cb])
            break

        if x < s:
            if visited[x][x] == 0:
                visited[x][x] = visited[x][cb] + 1
                queue.append((x, x))
            if visited[x + cb][cb] == 0 and x <= s:
                visited[x + cb][cb] = visited[x][cb] + 1
                queue.append((x + cb, cb))
            if visited[x - 1][cb] == 0 and x - 1 > 2:
                visited[x - 1][cb] = visited[x][cb] + 1
                queue.append((x - 1, cb))
        else:
            if visited[s][cb] and visited[s][cb] > visited[x][cb] + x - s:
                visited[s][cb] = visited[x][cb] + x - s
                queue.append((s, cb))


visited = [[0 for _ in range(2001)] for _ in range(2001)]
bfs()

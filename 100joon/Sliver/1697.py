from collections import deque


def bfs():
    queue = deque()
    queue.append((n, 0))
    while queue:
        x, cnt = queue.popleft()
        visited[x] = 1
        if x == k:
            print(cnt)
            return
        if 0 <= x - 1 and x - 1 not in visited:
            queue.append((x - 1, cnt + 1))
        if x * 2 <= abs(x + 1 - k) and x * 2 not in visited:
            queue.append((x * 2, cnt + 1))
        if x + 1 <= k and x + 1 not in visited:
            queue.append((x + 1, cnt + 1))


n, k = map(int, input().split())

visited = {}

bfs()

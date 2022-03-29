from collections import deque

n, k = map(int, input().split())


def bfs(n):
    queue = deque()
    queue.append(n)
    visited[n] = 0
    while queue:
        n = queue.popleft()
        if n == k:
            print(visited[k])
            break
        if n < k and visited[n * 2] == -1:
            queue.append(n * 2)
            visited[n * 2] = visited[n]
        if n - 1 >= 0 and visited[n - 1] == -1:
            queue.append(n - 1)
            visited[n - 1] = visited[n] + 1
        if n + 1 <= k and visited[n + 1] == -1:
            queue.append(n + 1)
            visited[n + 1] = visited[n] + 1


visited = [-1] * 200001


bfs(n)

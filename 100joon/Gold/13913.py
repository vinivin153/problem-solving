from collections import deque

n, k = map(int, input().split())


def bfs(n):
    queue = deque()
    queue.append((n, [n]))
    visited[n] = 0
    while queue:
        n, log = queue.popleft()
        if n == k:
            print(visited[k])
            print(*log)
            break
        if n < k and visited[n * 2] == -1:
            queue.append((n * 2, log + [n * 2]))
            visited[n * 2] = visited[n] + 1
        if n - 1 >= 0 and visited[n - 1] == -1:
            queue.append((n - 1, log + [n - 1]))
            visited[n - 1] = visited[n] + 1
        if n + 1 <= k and visited[n + 1] == -1:
            queue.append((n + 1, log + [n + 1]))
            visited[n + 1] = visited[n] + 1


visited = [-1] * (k * 2 + 1)
if n > k:
    print(n - k)
    for i in range(n, k - 1, -1):
        print(i, end=" ")
else:
    bfs(n)

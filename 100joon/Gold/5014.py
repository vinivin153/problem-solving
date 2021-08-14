from collections import deque


def bfs(F, S, G, U, D):
    queue = deque()
    queue.append((S, 0))
    visited = {}
    visited[S] = 1
    while queue:
        a, b = queue.popleft()
        if a == G:
            return b
        if a + U <= F and a + U not in visited:
            queue.append((a + U, b + 1))
            visited[a + U] = 1
        if 1 <= a - D and a - D not in visited:
            queue.append((a - D, b + 1))
            visited[a - D] = 1
    return "use the stairs"


F, S, G, U, D = map(int, input().split())


print(bfs(F, S, G, U, D))

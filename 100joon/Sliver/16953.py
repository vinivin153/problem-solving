from collections import deque


a, b = map(int, input().split())


def bfs(x, cnt):
    queue = deque()
    queue.append((x, cnt))
    visited.add(x)
    while queue:
        x, cnt = queue.popleft()
        if x == b:
            print(cnt)
            return
        t1 = x * 2
        t2 = x * 10 + 1
        if t1 <= b and t1 not in visited:
            queue.append((t1, cnt + 1))
        if t2 <= b and t2 not in visited:
            queue.append((t2, cnt + 1))

    print(-1)


visited = set()

bfs(a, 1)

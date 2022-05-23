from collections import deque


def bfs(n, target, tree):
    visited = [0] * (n + 1)
    queue = deque()
    queue.append(1)
    visited[1] = 1
    sum1 = 1
    while queue:
        x = queue.popleft()
        for y in tree[x]:
            if [x, y] == target or [y, x] == target:
                continue
            if visited[y] == 0:
                visited[y] = 1
                queue.append(y)
                sum1 += 1

    return abs(sum1 - (n - sum1))


def solution(n, wires):
    tree = [[] for _ in range(n + 1)]
    for a, b in wires:
        tree[a].append(b)
        tree[b].append(a)

    answer = 100
    for wire in wires:
        answer = min(answer, bfs(n, wire, tree))

    return answer

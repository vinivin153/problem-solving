from collections import deque


def solution(n, computers):
    answer = 0

    visited = [0] * 200

    def bfs(x):
        queue = deque()
        queue.append(x)
        visited[x] = 1
        while queue:
            current = queue.popleft()
            for i in range(n):
                if visited[i] == 0 and computers[current][i] == 1:
                    queue.append((i))
                    visited[i] = 1

    for i in range(n):
        if visited[i] == 0:
            bfs(i)
            answer += 1

    return answer

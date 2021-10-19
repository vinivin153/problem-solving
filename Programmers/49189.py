from collections import deque


def solution(n, edge):
    def bfs(x, dist):
        cnt = [0]
        queue = deque()
        queue.append((x, dist))
        visited[x] = 1
        while queue:
            x, dist = queue.popleft()
            try:
                cnt[dist] += 1
            except:
                cnt.append(1)
            for i in node[x]:
                if visited[i] == 0:
                    queue.append((i, dist + 1))
                    visited[i] = 1

        return cnt[-1]

    node = [[] for _ in range(n + 1)]

    for a, b in edge:
        node[a].append(b)
        node[b].append(a)

    visited = [0] * (n + 1)

    return bfs(1, 0)


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))

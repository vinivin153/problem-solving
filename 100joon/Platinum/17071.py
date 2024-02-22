from collections import deque

n, k = map(int, input().split())
MAX = 500000

visited = [[-1] * 2 for _ in range(MAX + 1)]
visited[n][0] = 0
queue = deque()
queue.append((n, 0))
pre = 0
while queue:
    current, cnt = queue.popleft()

    if pre != cnt:
        pre = cnt
        k += cnt
        if k > MAX:
            print(-1)
            break

    mod = cnt % 2
    if visited[k][mod] != -1:
        print(cnt)
        break

    for i in (current - 1, current + 1, current * 2):
        if 0 <= i <= MAX and visited[i][1 - mod] == -1:
            visited[i][1 - mod] = visited[current][mod] + 1
            queue.append((i, cnt + 1))

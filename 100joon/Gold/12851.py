import sys
from collections import deque

n, k = map(int, input().split())

if k <= n:
    print(n - k)
    print(1)
    sys.exit()

ans = 0
MAX = min(k * 2, 10**5 + 1)
visited = [MAX] * MAX
visited[n] = 0
queue = deque()
queue.append(n)
while queue:
    current = queue.popleft()

    for i in (current - 1, current + 1, current * 2):
        if 0 <= i < MAX:
            if i == k:
                if visited[current] + 1 == visited[k]:
                    ans += 1
                elif visited[current] + 1 < visited[k]:
                    visited[k] = visited[current] + 1
                    ans = 1
            elif visited[i] >= visited[current] + 1:
                visited[i] = visited[current] + 1
                queue.append(i)

print(visited[k])
print(ans)

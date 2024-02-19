import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
scv = list(map(int, input().split()))
visited = set()
queue = deque()
queue.append([scv, 0])
while queue:
    scv, cnt = queue.popleft()
    for hp in scv:
        if hp > 0:
            break
    else:
        print(cnt)
        break

    if len(scv) == 3:
        a, b, c = scv
        if (max(0, a - 9), max(0, b - 3), max(0, c - 1)) not in visited:
            queue.append([[max(0, a - 9), max(0, b - 3), max(0, c - 1)], cnt + 1])
            visited.add((max(0, a - 9), max(0, b - 3), max(0, c - 1)))

        if (max(0, a - 9), max(0, b - 1), max(0, c - 3)) not in visited:
            queue.append([[max(0, a - 9), max(0, b - 1), max(0, c - 3)], cnt + 1])
            visited.add((max(0, a - 9), max(0, b - 1), max(0, c - 3)))

        if (max(0, a - 3), max(0, b - 9), max(0, c - 1)) not in visited:
            queue.append([[max(0, a - 3), max(0, b - 9), max(0, c - 1)], cnt + 1])
            visited.add((max(0, a - 3), max(0, b - 9), max(0, c - 1)))

        if (max(0, a - 3), max(0, b - 1), max(0, c - 9)) not in visited:
            queue.append([[max(0, a - 3), max(0, b - 1), max(0, c - 9)], cnt + 1])
            visited.add((max(0, a - 3), max(0, b - 1), max(0, c - 9)))

        if (max(0, a - 1), max(0, b - 9), max(0, c - 3)) not in visited:
            queue.append([[max(0, a - 1), max(0, b - 9), max(0, c - 3)], cnt + 1])
            visited.add((max(0, a - 1), max(0, b - 9), max(0, c - 3)))

        if (max(0, a - 1), max(0, b - 3), max(0, c - 9)) not in visited:
            queue.append([[max(0, a - 1), max(0, b - 3), max(0, c - 9)], cnt + 1])
            visited.add((max(0, a - 1), max(0, b - 3), max(0, c - 9)))
    elif len(scv) == 2:
        a, b = scv
        if (max(0, a - 9), max(0, b - 3)) not in visited:
            queue.append([[max(0, a - 9), max(0, b - 3)], cnt + 1])
            visited.add((max(0, a - 9), max(0, b - 3)))

        if (max(0, a - 3), max(0, b - 9)) not in visited:
            queue.append([[max(0, a - 3), max(0, b - 9)], cnt + 1])
            visited.add((max(0, a - 3), max(0, b - 9)))
    else:
        if (max(0, scv[0] - 9)) not in visited:
            queue.append([[max(0, scv[0] - 9)], cnt + 1])
            visited.add((max(0, scv[0] - 9)))

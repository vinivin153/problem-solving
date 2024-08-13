import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
left = [0] + list(map(int, input().rstrip()))
right = [0] + list(map(int, input().rstrip()))


queue = deque()
queue.append((1, False, 1))
visited = set()
visited.add((1, False))
while queue:
    x, isRight, remove = queue.popleft()

    # 앞으로 한칸 전진하는 경우
    xx = x + 1
    if xx > n:
        print(1)
        break
    else:
        if (isRight and right[xx]) or (not isRight and left[xx]):
            if (xx, isRight) not in visited:
                queue.append((xx, isRight, remove + 1))
                visited.add((xx, isRight))

    # 뒤로 한칸 후진하는 경우
    xx = x - 1
    if xx > remove:
        if (isRight and right[xx]) or (not isRight and left[xx]):
            if (xx, isRight) not in visited:
                visited.add((xx, isRight))
                queue.append((xx, isRight, remove + 1))

    xx = x + k
    if xx > n:
        print(1)
        break
    else:
        # 반대편 줄로 넘어가는 경우
        if (not isRight and right[xx]) or (isRight and left[xx]):
            if (xx, not isRight) not in visited:
                visited.add((xx, not isRight))
                queue.append((xx, not isRight, remove + 1))
else:
    print(0)

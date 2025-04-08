import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
k = int(input())
apple = set()
for _ in range(k):
    a, b = map(int, input().split())
    apple.add((a - 1, b - 1))

l = int(input())
turn = deque()
for _ in range(l):
    a, b = input().rstrip().split()
    direction = 0
    direction = 3 if b == "L" else 1
    turn.append((int(a), direction))

# 북 동 남 서 (시계방향)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


time = 0
my = deque()
my_set = set()
my.append((0, 0))
my_set.add((0, 0))

stack = []
stack.append((0, 0, 1))
while stack:
    x, y, d = stack.pop()

    if turn and turn[0][0] == time:
        _, nd = turn.popleft()
        d = (d + nd) % 4

    time += 1
    nx = x + dx[d]
    ny = y + dy[d]

    if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in my_set:
        # 사과를 먹는 경우
        if (nx, ny) in apple:
            apple.remove((nx, ny))
        else:  # 일반 이동
            a, b = my.popleft()
            my_set.remove((a, b))

        my.append((nx, ny))
        my_set.add((nx, ny))
        stack.append((nx, ny, d))

print(time)

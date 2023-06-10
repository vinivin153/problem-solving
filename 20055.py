import sys
from collections import deque

input = sys.stdin.readline


n, k = map(int, input().split())
durability = deque(list(map(int, input().split())))
robot = deque([False] * n)
cnt = 0
ans = 0


def rotate():
    durability.appendleft(durability.pop())
    robot.pop()
    robot.appendleft(False)
    robot[-1] = False


def move_robot():
    for i in range(n - 2, -1, -1):
        if robot[i] and not robot[i + 1] and durability[i + 1] > 0:
            robot[i] = False
            robot[i + 1] = True
            durability[i + 1] -= 1
            check_count(i + 1)


def add_robot():
    if durability[0] > 0:
        durability[0] -= 1
        check_count(0)
        robot[0] = True


def check_count(idx):
    global cnt
    if durability[idx] == 0:
        cnt += 1


while cnt < k:
    ans += 1
    rotate()
    move_robot()
    add_robot()

print(ans)

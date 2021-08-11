import sys
from collections import deque

n, m = map(int, input().split())

queue1 = deque()
queue2 = deque()
ground1 = deque()
ground2 = deque()

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    queue1.append(a)
    queue2.append(b)


for turn in range(m):
    if turn % 2 == 0:
        ground1.append(queue1.pop())
        if not queue1:
            print("su")
            sys.exit()
    else:
        ground2.append(queue2.pop())
        if not queue2:
            print("do")
            sys.exit()

    if ground1 and ground2:
        if ground1[-1] + ground2[-1] == 5:
            queue2.extendleft(ground1)
            queue2.extendleft(ground2)
            ground1.clear()
            ground2.clear()
        elif ground1[-1] == 5 or ground2[-1] == 5:
            queue1.extendleft(ground2)
            queue1.extendleft(ground1)
            ground1.clear()
            ground2.clear()
    elif ground1:
        if ground1[-1] == 5:
            queue1.extendleft(ground2)
            queue1.extendleft(ground1)
            ground1.clear()
            ground2.clear()
    else:
        if ground2[-1] == 5:
            queue1.extendleft(ground2)
            queue1.extendleft(ground1)
            ground1.clear()
            ground2.clear()


a = len(queue1)
b = len(queue2)

if a == b:
    print("dosu")
elif a > b:
    print("do")
else:
    print("su")

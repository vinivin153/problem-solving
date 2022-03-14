import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
queue = deque()
for _ in range(n):
    func = input().rstrip().split()
    if func[0] == "push":
        queue.append(int(func[1]))
    elif func[0] == "pop":
        print(queue.popleft()) if queue else print(-1)
    elif func[0] == "size":
        print(len(queue))
    elif func[0] == "empty":
        print(0) if queue else print(1)
    elif func[0] == "front":
        print(queue[0]) if queue else print(-1)
    elif func[0] == "back":
        print(queue[-1]) if queue else print(-1)

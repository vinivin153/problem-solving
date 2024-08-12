import sys
from collections import deque

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    p = list(input().rstrip())
    n = int(input())
    arr = deque(input().split(","))
    arr[0] = arr[0][1:]
    arr[-1] = arr[-1][:-2]
    if arr[0] == "":
        arr.pop()
    reverse = False
    for i in p:
        if i == "R":
            reverse = not reverse
        elif i == "D":
            if arr:
                if reverse:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                print("error")
                break
    else:
        if reverse:
            print("[", end="")
            while arr:
                print(arr.pop(), end="")
                if arr:
                    print(",", end="")
            print("]")
        else:
            print("[", end="")
            while arr:
                print(arr.popleft(), end="")
                if arr:
                    print(",", end="")
            print("]")

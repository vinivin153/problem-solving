import sys

input = sys.stdin.readline

n = int(input())
res = 0
for _ in range(n):
    word = input().rstrip()
    stack = []
    for i in word:
        if not stack:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    if not stack:
        res += 1

print(res)

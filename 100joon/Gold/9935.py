import sys

input = sys.stdin.readline
str1 = input().rstrip()
bomb = input().rstrip()
b = len(bomb)

stack = []

for i in str1:
    stack.append(i)

    if stack[-1] == bomb[-1]:
        if len(stack) >= b:
            for i in range(1, b + 1):
                if stack[-1 * i] != bomb[-1 * i]:
                    break
            else:
                for _ in range(b):
                    stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")

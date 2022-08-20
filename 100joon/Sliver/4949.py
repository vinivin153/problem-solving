import sys

input = sys.stdin.readline

s = input().rstrip()
while s != ".":
    flag = 1
    stack = []
    for i in s:
        if i == "(" or i == "[":
            stack.append(i)
            continue

        if i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                flag = 0
                break
        elif i == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                flag = 0
                break

    if stack:
        flag = 0

    if flag:
        print("yes")
    else:
        print("no")

    s = input().rstrip()

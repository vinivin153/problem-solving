import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

p = [-1]
stack = [arr[n - 1]]
for i in range(n - 2, -1, -1):
    if arr[i] < stack[-1]:
        p.append(stack[-1])
        stack.append(arr[i])
    else:
        if arr[i] >= stack[0]:
            stack = [arr[i]]
            p.append(-1)
        else:
            while stack[-1] <= arr[i]:
                stack.pop()
            p.append(stack[-1])
            stack.append(arr[i])

print(*p[::-1])

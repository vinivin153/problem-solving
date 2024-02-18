import sys

input = sys.stdin.readline
n = int(input())
arr = input().rstrip()

ans = []
stack = []
stack.append([1, [arr[0]]])
while stack:
    idx, k = stack.pop()
    s = arr[idx : idx + 2]
    if idx == n:
        if len(k) == 1:
            ans.append(eval(k[0] + s))
        else:
            ans.append(eval(str(eval("".join(k))) + s))
            ans.append(eval("".join(k[:-1]) + str(eval(k[-1] + s))))
        continue

    ss = [arr[idx], arr[idx + 1]]
    if len(k) == 1:
        stack.append([idx + 2, k + ss])
    else:
        stack.append([idx + 2, [str(eval("".join(k[:-1]) + str(eval(k[-1] + s))))]])
        stack.append([idx + 2, [str(eval("".join(k)))] + ss])

print(max(ans))

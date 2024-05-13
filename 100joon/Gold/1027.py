import sys

input = sys.stdin.readline

MIN = -1 * 10**10
n = int(input())
arr = list(map(int, input().split()))


def gradient(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)


ans = 0
for start in range(n):
    pre = MIN
    cnt1 = 0
    cnt2 = 0
    for end in range(start + 1, n):
        g = gradient(start, arr[start], end, arr[end])
        if g > pre:
            cnt1 += 1
            pre = g

    pre = MIN * -1
    for end in range(start - 1, -1, -1):
        g = gradient(end, arr[end], start, arr[start])
        if g < pre:
            cnt2 += 1
            pre = g
    ans = max(ans, cnt1 + cnt2)

print(ans)

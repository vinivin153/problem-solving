import sys

input = sys.stdin.readline

n = int(input())
sb = [list(map(int, input().split())) for _ in range(n)]
ans = sys.maxsize
for mask in range(1, 1 << n):
    ss, bb = 1, 0
    for i in range(n):
        if (1 << i) & mask:
            ss *= sb[i][0]
            bb += sb[i][1]
    ans = min(abs(ss - bb), ans)

print(ans)

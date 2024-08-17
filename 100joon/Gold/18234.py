import sys

input = sys.stdin.readline
n, t = map(int, input().split())
carrots = sorted(
    [list(map(int, input().split())) for _ in range(n)], key=lambda x: x[1]
)

ans = 0
day = t - n
for w, p in carrots:
    ans += w + p * day
    day += 1

print(ans)

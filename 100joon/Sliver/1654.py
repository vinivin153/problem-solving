import sys

input = sys.stdin.readline
k, n = map(int, input().split())
line = [int(input().rstrip()) for _ in range(k)]

start = 1
end = max(line)
while start <= end:
    cnt = 0
    mid = (start + end) // 2

    for i in line:
        cnt += i // mid

    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)

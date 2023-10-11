import sys

input = sys.stdin.readline

n, m = map(int, input().split())
trees = sorted(list(map(int, input().split())), reverse=True)

start = 0
last = max(trees)
ans = 0

while start <= last:
    mid = (start + last) // 2
    sum_tree = 0
    for tree in trees:
        diff = tree - mid

        if diff <= 0:
            break

        sum_tree += diff

    if sum_tree >= m:
        ans = mid
        start = mid + 1
    else:
        last = mid - 1

print(ans)

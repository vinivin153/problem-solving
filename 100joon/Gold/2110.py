import sys

n, c = map(int, input().split())
houses = []

for _ in range(n):
    houses.append(int(input()))

houses.sort()

min_dist = 1
max_dist = houses[-1] - houses[0]
ans = 1

while min_dist <= max_dist:
    mid_dist = (min_dist + max_dist) // 2
    recent = houses[0]
    cnt = 1

    for i in range(1, n):
        if houses[i] - recent >= mid_dist:
            recent = houses[i]
            cnt += 1

    if cnt < c:
        max_dist = mid_dist - 1
    else:
        ans = mid_dist
        min_dist = mid_dist + 1

print(ans)

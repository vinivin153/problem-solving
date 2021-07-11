import sys
from itertools import combinations

n, m = map(int, input().split())
city = []
for _ in range(n):
    city.append(list(map(int, sys.stdin.readline().split())))

home = []
chicken = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            home.append([i, j])
        elif city[i][j] == 2:
            chicken.append([i, j])

city_dist = [[] for _ in range(len(home))]
cnt = 0
for x1, y1 in home:
    for x2, y2 in chicken:
        city_dist[cnt].append(abs(x2 - x1) + abs(y2 - y1))
    cnt += 1

case = list(combinations(range(len(chicken)), m))

min_dist = sys.maxsize

for j in case:
    sum_pick = 0
    for i in range(cnt):
        pick = sys.maxsize
        for k in range(len(chicken)):
            if k in j:
                pick = min(pick, city_dist[i][k])
        sum_pick += pick
    min_dist = min(min_dist, sum_pick)

print(min_dist)

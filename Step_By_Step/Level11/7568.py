import sys

num = int(input())
chart = []
rank = [1 for i in range(num)]

for _ in range(num):
    chart.append(list(map(int, sys.stdin.readline().split())))

for i in range(num - 1):
    for j in range(i + 1, num):
        if chart[i][0] < chart[j][0] and chart[i][1] < chart[j][1]:
            rank[i] += 1
        elif chart[i][0] > chart[j][0] and chart[i][1] > chart[j][1]:
            rank[j] += 1

print(*rank)

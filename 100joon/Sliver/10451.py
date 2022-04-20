import sys

input = sys.stdin.readline


def cycle(x):
    while not visited[x]:
        visited[x] = v[x]
        x = v[x]


t = int(input())
for _ in range(t):
    n = int(input())
    v = [0] + list(map(int, input().split()))
    cnt = 0
    visited = [0] * (n + 1)
    for i in range(1, n + 1):
        if visited[i] == 0:
            cycle(i)
            cnt += 1
    print(cnt)

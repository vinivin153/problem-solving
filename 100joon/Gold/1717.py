import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline
n, m = map(int, input().split())

parent = [i for i in range(n + 1)]


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(a, b):
    x = find_parent(a)
    y = find_parent(b)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


for _ in range(m):
    t, a, b = map(int, input().split())
    # 합집합
    if t == 0:
        union(a, b)
    else:
        p1 = find_parent(a)
        p2 = find_parent(b)
        if p1 == p2:
            print("YES")
        else:
            print("NO")

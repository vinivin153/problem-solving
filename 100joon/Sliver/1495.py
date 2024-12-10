import sys

input = sys.stdin.readline

n, s, m = map(int, input().split())
v = list(map(int, input().split()))

v_set = set({s})
for i in range(n):
    new_v = set()
    for j in v_set:
        if j - v[i] >= 0:
            new_v.add(j - v[i])
        if j + v[i] <= m:
            new_v.add(j + v[i])
    v_set = new_v
    
if v_set:
    print(max(v_set))
else:
    print(-1)
    
    

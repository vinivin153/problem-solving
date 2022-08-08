import sys

input = sys.stdin.readline

n, s, r = map(int, input().split())
cracked = set(map(int, input().split()))
t = set(cracked)
extra = set(map(int, input().split()))
res = 0

for boat in t:
    if boat in extra:
        extra.remove(boat)
        cracked.remove(boat)

for boat in cracked:
    if boat - 1 in extra:
        extra.remove(boat - 1)
    elif boat + 1 in extra:
        extra.remove(boat + 1)
    else:
        res += 1

print(res)

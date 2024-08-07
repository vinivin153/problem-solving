a, b, c, m = map(int, input().split())
fatigue = 0
work = 0
for i in range(24):
    if a + fatigue > m:
        fatigue = max(0, fatigue - c)
    else:
        fatigue += a
        work += b

print(work)

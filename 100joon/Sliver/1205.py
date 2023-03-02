import sys

n, score, p = map(int, input().split())
if n == 0:
    print(1)
    sys.exit()
scores = list(map(int, input().split()))

rank = [1] * (n + 1)
for i in range(1, n):
    if scores[i] == scores[i - 1]:
        rank[i] = rank[i - 1]
    else:
        rank[i] = i + 1

for i in range(n):
    if scores[i] < score:
        if 0 <= i - 1 and scores[i - 1] == score:
            print(rank[i - 1])
            break
        else:
            print(i + 1)
            break
else:
    if n != p:
        if scores[n - 1] == score:
            print(rank[n - 1])
        else:
            print(n + 1)
    else:
        print(-1)

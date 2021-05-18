import sys

n, k = map(int, sys.stdin.readline().split())

medal = []
save_info = None

for _ in range(n):
    num, *tmp = map(int, sys.stdin.readline().split())
    if num == k:
        save_info = tmp
    medal.append(tmp)

medal.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)

print(medal.index(save_info) + 1)

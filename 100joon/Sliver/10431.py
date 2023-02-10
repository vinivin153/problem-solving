import sys

input = sys.stdin.readline
t = int(input())
for n in range(t):
    num, *line = map(int, input().split())
    new_line = []
    cnt = 0
    for i in line:
        for idx, v in enumerate(new_line):
            if i < v:
                cnt += len(new_line) - idx
                new_line.insert(idx, i)
                break
        else:
            new_line.append(i)
    print(n + 1, cnt)

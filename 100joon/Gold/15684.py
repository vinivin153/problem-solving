import sys

input = sys.stdin.readline

n, m, h = map(int, input().split())
line = [{} for _ in range(h + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    line[a][b] = b + 1
    line[a][b + 1] = b


def isCorrect():
    for j in range(1, n + 1):
        now = j
        for i in range(1, h + 1):
            if now in line[i]:
                now = line[i][now]

        if now != j:
            return False
    return True


answer = 4


def backtracking(cnt, height, k):
    global answer
    if isCorrect():
        answer = min(cnt, answer)
        return

    if cnt == answer - 1 or answer <= cnt:
        return

    for i in range(height, h + 1):
        if i != height:
            k = 1
        for j in range(k, n):
            if not ((j in line[i]) or ((j + 1) in line[i])):
                line[i][j] = j + 1
                line[i][j + 1] = j
                backtracking(cnt + 1, i, j + 2)
                del line[i][j]
                del line[i][j + 1]


backtracking(0, 1, 1)
if answer == 4:
    print(-1)
else:
    print(answer)

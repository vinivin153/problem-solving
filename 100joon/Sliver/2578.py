b = {}
for i in range(5):
    a = list(map(int, input().split()))
    for j in range(5):
        b[a[j]] = [i, j]

bingo = [[0 for _ in range(5)] for _ in range(5)]

answer = []
cnt = 0
for i in range(5):
    answer += list(map(int, input().split()))
for n in answer:
    cnt += 1
    res = 0
    bingo[b[n][0]][b[n][1]] = 1

    s = [0] * 5
    for i in range(5):
        if sum(bingo[i]) == 5:
            res += 1
        for j in range(5):
            s[j] += bingo[i][j]
    for i in range(5):
        if s[i] == 5:
            res += 1
    if bingo[0][0] + bingo[1][1] + bingo[2][2] + bingo[3][3] + bingo[4][4] == 5:
        res += 1
    if bingo[0][4] + bingo[1][3] + bingo[2][2] + bingo[3][1] + bingo[4][0] == 5:
        res += 1

    if res >= 3:
        print(cnt)
        break

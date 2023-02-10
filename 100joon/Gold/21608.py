import sys

input = sys.stdin.readline

n = int(input())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

mat = [[0] * n for _ in range(n)]
ans = 0
student = {}
for _ in range(n ** 2):
    num, *love = map(int, input().split())
    student[num] = set(love)
    max_score = -1
    max_loc = [0, 0]
    for x in range(n):
        for y in range(n):
            if mat[x][y] == 0:
                love_cnt = 0
                blank = 0
                for i in range(4):
                    nx = dx[i] + x
                    ny = dy[i] + y
                    if 0 <= nx < n and 0 <= ny < n:
                        if mat[nx][ny] in student[num]:
                            love_cnt += 1
                        elif mat[nx][ny] == 0:
                            blank += 1
                score = love_cnt * 10 + blank
                if max_score < score:
                    max_score = score
                    max_loc = [x, y]
    mat[max_loc[0]][max_loc[1]] = num

for x in range(n):
    for y in range(n):
        love_cnt = 0
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < n:
                if mat[nx][ny] in student[mat[x][y]]:
                    love_cnt += 1
        ans += int(10 ** (love_cnt - 1))
print(ans)

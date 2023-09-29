import sys

input = sys.stdin.readline
from collections import deque
from itertools import combinations

n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def find_group():
    visited = [[False] * n for _ in range(n)]
    gnumber = -1
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                gnumber += 1
                cnt = 0
                origin = mat[i][j]
                group_num.append(origin)
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True
                while queue:
                    x, y = queue.popleft()
                    group_mat[x][y] = gnumber
                    cnt += 1
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < n:
                            if not visited[nx][ny] and mat[nx][ny] == origin:
                                queue.append((nx, ny))
                                visited[nx][ny] = True
                group_cnt.append(cnt)


def find_kiss():
    for x in range(n):
        for y in range(n):
            for i in range(2):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if mat[x][y] != mat[nx][ny]:
                        kiss[group_mat[x][y]][group_mat[nx][ny]] += 1
                        kiss[group_mat[nx][ny]][group_mat[x][y]] += 1


def calc_score():
    score = 0
    for a, b in combinations(range(len(group_cnt)), 2):
        score += (
            (group_cnt[a] + group_cnt[b]) * group_num[a] * group_num[b] * kiss[a][b]
        )
    return score


def rotate():
    mid = n // 2
    temp = []
    for i in range(n):
        temp.append(mat[i][mid])

    for i in range(n):
        mat[n - i - 1][mid] = mat[mid][i]

    mat[mid] = temp

    rotate_square(0, 0)
    rotate_square(mid + 1, 0)
    rotate_square(0, mid + 1)
    rotate_square(mid + 1, mid + 1)


def rotate_square(x, y):
    mid = n // 2
    new_mat = []
    for i in range(x, x + mid):
        new_mat.append(mat[i][y : y + mid])

    for i, j in enumerate(zip(*new_mat), x):
        mat[i][y : y + mid] = reversed(j)


group_mat = [[0] * n for _ in range(n)]
group_cnt = []
group_num = []
find_group()
kiss = [[0] * len(group_cnt) for _ in range(len(group_cnt))]
find_kiss()
ans = calc_score()
for _ in range(3):
    rotate()

    group_mat = [[0] * n for _ in range(n)]
    group_cnt = []
    group_num = []
    find_group()

    kiss = [[0] * len(group_cnt) for _ in range(len(group_cnt))]
    find_kiss()
    ans += calc_score()
print(ans)

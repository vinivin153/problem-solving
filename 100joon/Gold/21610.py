import sys


def move_cloud(d, num, cloud):
    direction = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
    for i in range(len(cloud)):
        cloud[i][0] = (cloud[i][0] + direction[d][0] * num) % n
        cloud[i][1] = (cloud[i][1] + direction[d][1] * num) % n


def rain():
    for r, c in cloud:
        basket[r][c] += 1


def copy_magic():
    for r, c in cloud:
        cnt = 0
        if r - 1 >= 0 and c - 1 >= 0 and basket[r - 1][c - 1] > 0:
            cnt += 1
        if r - 1 >= 0 and c + 1 < n and basket[r - 1][c + 1] > 0:
            cnt += 1
        if r + 1 < n and c - 1 >= 0 and basket[r + 1][c - 1] > 0:
            cnt += 1
        if r + 1 < n and c + 1 < n and basket[r + 1][c + 1] > 0:
            cnt += 1
        basket[r][c] += cnt


def make_cloud():
    old_cloud = set()
    for a, b in cloud:
        old_cloud.add((a, b))
    new_cloud = []
    for i in range(n):
        for j in range(n):
            if (i, j) not in old_cloud and basket[i][j] >= 2:
                new_cloud.append([i, j])
                basket[i][j] -= 2
    return new_cloud


n, m = map(int, sys.stdin.readline().split())

basket = []
for _ in range(n):
    basket.append(list(map(int, sys.stdin.readline().split())))

cloud = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]]

for _ in range(m):
    d, c = map(int, sys.stdin.readline().split())
    move_cloud(d - 1, c, cloud)
    rain()
    copy_magic()
    cloud = make_cloud()

cnt = 0
for i in basket:
    cnt += sum(i)

print(cnt)

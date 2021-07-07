n, m = map(int, input().split())
x, y, w = map(int, input().split())
cnt = 0

map_data = []
for i in range(n):
    map_data.append(list(map(int, input().split())))

visited = [[0] * m for i in range(n)]
visited[x][y] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while True:
    for i in range(4):
        w -= 1
        if w < 0:
            w = 3
        v1 = dx[w] + x
        v2 = dy[w] + y
        if map_data[dx[w] + x][dy[w] + y] == 0 and visited[dx[w] + x][dy[w] + y] == 0:
            x = dx[w] + x
            y = dy[w] + y
            visited[x][y] = 1
            break
    else:
        x = x - dx[w]
        y = y - dy[w]
        if map_data[x][y] == 1:
            break

for i in visited:
    cnt += i.count(1)

print(cnt)

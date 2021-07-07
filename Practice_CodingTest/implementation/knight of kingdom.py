y, x = input()
y = int(ord(y) - 96)
x = int(x)
cnt = 0

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

for i in range(8):
    if 1 <= dx[i] + x <= 8 and 1 <= dy[i] + y <= 8:
        cnt += 1

print(cnt)

import sys

n = int(sys.stdin.readline())
size = 2 * n - 1

arr = [[" " for i in range(size)] for j in range(n)]


def star(row, col, n):
    if n == 3:
        arr[row][col] = "*"
        arr[row + 1][col - 1] = "*"
        arr[row + 1][col + 1] = "*"
        arr[row + 2][col - 2 : col + 3] = ["*", "*", "*", "*", "*"]
    else:
        k = n // 2
        star(row, col, k)
        star(row + k, col - k, k)
        star(row + k, col + k, k)


star(0, size // 2, n)

for i in arr:
    print("".join(i))

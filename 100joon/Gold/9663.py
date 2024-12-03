# 16:00 시작

n = int(input())

cols = [False] * n
cross1 = [False] * (2 * n - 1)
cross2 = [False] * (2 * n - 1)
ans = 0


def backtracking(row):
    global ans
    if row == n:
        ans += 1
        return

    for col in range(n):
        if not cols[col] and not cross1[row + col] and not cross2[row - col + n - 1]:
            cols[col] = cross1[row + col] = cross2[row - col + n - 1] = True
            backtracking(row + 1)
            cols[col] = cross1[row + col] = cross2[row - col + n - 1] = False


backtracking(0)
print(ans)

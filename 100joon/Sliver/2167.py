n, m = map(int, input().split())
mat = [[0] * (m + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]

prefixsum = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        prefixsum[i][j] = (
            prefixsum[i - 1][j]
            + prefixsum[i][j - 1]
            - prefixsum[i - 1][j - 1]
            + mat[i][j]
        )


for i in range(int(input())):
    r1, c1, r2, c2 = map(int, input().split())
    print(
        prefixsum[r2][c2]
        - prefixsum[r2][c1 - 1]
        - prefixsum[r1 - 1][c2]
        + prefixsum[r1 - 1][c1 - 1]
    )

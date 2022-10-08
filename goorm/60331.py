n = int(input())
mat = [[" "] * (n) for _ in range(n)]

mat[0] = ["#"] * n


def recusion(s, e):
    if s > e:
        return

    for i in range(s, e):
        mat[s][i] = "#"
        mat[n - s - 1][i] = "#"
        mat[i][s] = "#"
        mat[i][n - s - 1] = "#"

    mat[s + 1][s] = " "
    mat[s + 2][s + 1] = "#"
    recusion(s + 2, e - 2)


recusion(0, n)

for i in mat:
    print(*i)

n, m, k = map(int, input().split())
mat = [list(input().rstrip()) for _ in range(n)]

for i in range(n):
    for _ in range(k):
        for j in range(m):
            for _ in range(k):
                print(mat[i][j], end="")
        print()

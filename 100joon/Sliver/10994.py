n = int(input())
m = 4 * n - 3

mat = [[" "] * m for _ in range(m)]
# c는 중첩횟수
# k는 별의 수
# start는 2씩 증가
# k는 4씩 감소
def star(cnt, start, k):

    for i in range(k):
        # 위
        mat[start][start + i] = "*"
        # 왼쪽
        mat[start + i][start] = "*"
        # 아래
        mat[start + k - 1][start + i] = "*"
        # 오른쪽
        mat[start + i][start + k - 1] = "*"

    if cnt == n:
        return
    star(cnt + 1, start + 2, k - 4)


star(1, 0, m)

for i in mat:
    print("".join(i))

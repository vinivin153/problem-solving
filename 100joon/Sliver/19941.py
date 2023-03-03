import sys

input = sys.stdin.readline

n, k = map(int, input().split())
table = list(input().rstrip())

cnt = 0
for i in range(n):
    # 사람인 경우
    if table[i] == "P":
        for p in range(i - k, i + k + 1):
            if 0 <= p < n and table[p] == "H":
                table[p] = "_"
                cnt += 1
                break

print(cnt)

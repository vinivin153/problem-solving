import sys

n = int(sys.stdin.readline())
stair = [0]
for _ in range(n):
    stair.append(int(sys.stdin.readline()))


dp = [0 for _ in range(n + 1)]
dp[1] = stair[1]
if n > 1:
    dp[2] = dp[1] + stair[2]

for i in range(3, n + 1):
    dp[i] = stair[i] + max(dp[i - 3] + stair[i - 1], dp[i - 2])

print(dp[n])

# 가장 작은 부분에서 보이는 규칙만을 적용하자

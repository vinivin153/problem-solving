n = int(input())

food_cage = list(map(int, input().split()))

dp = [0] * (n + 1)
dp[1], dp[2] = food_cage[0], food_cage[1]

for i in range(3, n + 1):
    dp[i] = max(dp[i - 1], dp[i - 2] + food_cage[i - 1])

print(dp[n])

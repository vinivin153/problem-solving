n = int(input())
dp = [0] * (n + 1)


def fibonacci(x):
    if x == 1 or x == 2:
        return 1
    if dp[x] != 0:
        return dp[x]
    dp[x] = fibonacci(x - 1) + fibonacci(x - 2)
    return dp[x]


print(fibonacci(n))

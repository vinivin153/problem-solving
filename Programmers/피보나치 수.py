import sys

sys.setrecursionlimit(10**8)


def solution(n):
    memo = [0] * (n + 1)
    memo[1] = 1

    def fibo(n):
        if n in (0, 1):
            return memo[n]

        if not memo[n - 1]:
            memo[n - 1] = fibo(n - 1) % 1234567

        if not memo[n - 2]:
            memo[n - 2] = fibo(n - 2) % 1234567

        memo[n] = (memo[n - 1] + memo[n - 2]) % 1234567

        return memo[n]

    return fibo(n)

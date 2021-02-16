n, m = map(int, input().split())
a = list(map(int, input().split()))


def blackjack():
    max_score = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                t = a[i] + a[j] + a[k]
                if t == m:
                    return t
                elif t < m and t > max_score:
                    max_score = t
    return max_score


print(blackjack())
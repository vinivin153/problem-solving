def solution(n, k):
    facto = [1] * n
    for i in range(2, n):
        facto[i] = facto[i - 1] * i

    nums = [i for i in range(1, n + 1)]
    answer = []
    k -= 1
    while n:
        q = k // facto[n - 1]
        answer.append(nums.pop(q))
        k %= facto[n - 1]
        n -= 1

    return answer

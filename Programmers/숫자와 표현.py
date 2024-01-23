def solution(n):
    nums = [i for i in range(1, n + 1)]
    start = 0
    end = 0
    total = 1
    ans = 0
    while start < n - 1 and end < n - 1:
        if total > n:
            total -= nums[start]
            start += 1
        else:
            if total == n:
                ans += 1
            end += 1
            total += nums[end]

    return ans + 1

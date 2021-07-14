n = int(input())
nums = list(map(int, input().split()))

visited = [0 for _ in range(n)]
result = 0
picked = []


def dfs():
    global result
    if len(picked) == n:
        hap = 0
        for i in range(n - 1):
            hap += abs(picked[i] - picked[i + 1])
        result = max(hap, result)
    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                picked.append(nums[i])
                dfs()
                visited[i] = 0
                picked.pop()


dfs()
print(result)

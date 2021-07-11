def backTracking(cnt, idx):
    if cnt == 6:
        for i in range(49):
            if visited[i] == 1:
                print(nums[i], end=" ")
        print()
    else:
        for i in range(idx, n):
            if visited[i] == 1:
                continue
            visited[i] = 1
            backTracking(cnt + 1, i + 1)
            visited[i] = 0


while True:
    visited = [0] * 50
    n, *nums = map(int, input().split())
    if n == 0:
        break
    backTracking(0, 0)
    print()

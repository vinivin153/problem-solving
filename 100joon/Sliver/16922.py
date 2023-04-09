n = int(input())

nums = [1, 5, 10, 50]
num_set = set()


def dfs(cnt, sum_nums, idx):
    global num_set
    if cnt == n:
        num_set.add(sum_nums)
        return

    for i in range(idx, 4):
        dfs(cnt + 1, sum_nums + nums[i], i)


dfs(0, 0, 0)
print(len(num_set))

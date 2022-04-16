import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
operation = list(map(int, input().split()))

visited = [0] * (n - 1)
func = []
for i in range(4):
    func = func + [i] * operation[i]


res = []

max_val = -1000000000
min_val = 1000000000


def backtracking(val, cnt):
    global min_val, max_val
    if cnt == n - 1:
        if val > max_val:
            max_val = val
        if val < min_val:
            min_val = val
        return
    for i in range(n - 1):
        if visited[i] == 0:
            visited[i] = 1
            if func[i] == 0:
                backtracking(val + nums[cnt + 1], cnt + 1)
            elif func[i] == 1:
                backtracking(val - nums[cnt + 1], cnt + 1)
            elif func[i] == 2:
                backtracking(val * nums[cnt + 1], cnt + 1)
            elif func[i] == 3:
                backtracking(int(val / nums[cnt + 1]), cnt + 1)
            visited[i] = 0


backtracking(nums[0], 0)
print(max_val)
print(min_val)

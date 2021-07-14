def eratos(n):
    k = int(n ** 0.5) + 1
    for i in range(2, k + 1):
        if s[i] == 1:
            for j in range(i + i, n, i):
                s[j] = 0
    for i in range(3, n, 2):
        if s[i] == 1:
            p_nums[i] = 1


test_case = []
while True:
    n = int(input())
    if n == 0:
        break
    test_case.append(n)

n = max(test_case)

s = [1 for _ in range(n)]
p_nums = {}
eratos(n)

for t in test_case:
    if t == 0:
        break
    for i in p_nums.keys():
        if (t - i) in p_nums:
            print(f"{t} = {i} + {t-i}")
            break
    else:
        print("Goldbach's conjecture is wrong.")

num = int(input())
if num == 1:
    print(1)
    exit()
i = 1
dp = [1]
while True:
    if num <= dp[i - 1] + 6 * i:
        print(i + 1)
        break
    else:
        dp.append(dp[i - 1] + 6 * i)
        i += 1

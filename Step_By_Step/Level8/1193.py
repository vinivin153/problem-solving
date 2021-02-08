num = int(input())
i = 1
s = 1
while True:
    if num <= s:
        if i % 2 == 0:
            print(f"{i-(s-num)}/{s-num+1}")
        else:
            print(f"{s-num+1}/{i-(s-num)}")
        break
    else:
        i += 1
        s += i

name = input()

l = len(name)
alpha = {}
for i in name:
    if i in alpha:
        alpha[i] += 1
    else:
        alpha[i] = 1

alpha = sorted(alpha.items())
flag = 0
res = ""
center = ""
for al, num in alpha:
    if num % 2 == 0:
        res = res + al * (num // 2)
    elif num % 2 == 1 and flag == 0:
        flag = 1
        center = al
        res = res + al * (num // 2)
    else:
        print("I'm Sorry Hansoo")
        break
else:
    print(res + center + res[::-1])

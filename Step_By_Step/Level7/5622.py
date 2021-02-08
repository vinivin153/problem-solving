s = input()
sum = 0
for i in s:
    if i <= "O":
        sum += (ord(i) - 65) // 3 + 3
    elif "P" <= i <= "S":
        sum += 8
    elif "T" <= i <= "V":
        sum += 9
    else:
        sum += 10
print(sum)
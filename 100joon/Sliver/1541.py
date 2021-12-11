cal = input()

pre = 0
result = 0
idx = len(cal)
for i in range(len(cal)):
    if cal[i] == "+":
        result += int(cal[pre:i])
        pre = i + 1
    elif cal[i] == "-":
        idx = i + 1
        result += int(cal[pre:i])
        pre = i + 1
        break

for i in range(idx, len(cal)):
    if cal[i] == "-" or cal[i] == "+":
        result -= int(cal[pre:i])
        pre = i + 1
if idx == len(cal):
    result += int(cal[pre:])
else:
    result -= int(cal[pre:])


print(result)

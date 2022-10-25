# 폴더 폰 자판
keyboard = [
    "0",
    ["1", ".", ",", "?", "!"],
    ["2", "A", "B", "C"],
    ["3", "D", "E", "F"],
    ["4", "G", "H", "I"],
    ["5", "J", "K", "L"],
    ["6", "M", "N", "O"],
    ["7", "P", "Q", "R", "S"],
    ["8", "T", "U", "V"],
    ["9", "W", "X", "Y", "Z"],
]
n = int(input())
s = list(input().rstrip())

res = ""
cnt = 1
for i in range(n - 1):
    current_num = int(s[i])
    next_num = int(s[i + 1])
    if current_num != next_num:
        res += keyboard[current_num][cnt % len(keyboard[current_num]) - 1]
        cnt = 1
    else:
        cnt += 1

res += keyboard[int(s[n - 1])][cnt % len(keyboard[int(s[n - 1])]) - 1]
print(res)

import sys

input = sys.stdin.readline

word = input().rstrip()
vowels = ("a", "e", "i", "o", "u")

while word != "end":
    pre = ""
    flag = 0
    check = -1
    cnt = 0
    for i in word:
        if i in vowels:
            flag = 1
            if cnt > 0:
                cnt += 1
            else:
                cnt = 1
        else:
            if cnt < 0:
                cnt -= 1
            else:
                cnt = -1

        if i == pre and i != "e" and i != "o":
            flag = 0
            break

        pre = i
        if abs(cnt) > 2:
            flag = 0
            break

    if flag:
        print(f"<{word}> is acceptable.")
    else:
        print(f"<{word}> is not acceptable.")
    word = input().rstrip()

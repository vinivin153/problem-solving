import sys

arry = list(sys.stdin.readline())
cnt = arry.count(" ")
if arry[0] == " ":
    cnt -= 1
if arry[-2] == " ":
    cnt -= 1
print(cnt + 1)

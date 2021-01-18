import sys

num = int(sys.stdin.readline())
for i in range(num):
    count = 1
    score = 0
    a = list(sys.stdin.readline())
    for j in range(len(a)):
        if a[j] == "O":
            score += count
            count += 1
        else:
            count = 1
    print(score)

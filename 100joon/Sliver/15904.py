import sys

s = list(sys.stdin.readline().rstrip())

word = ["U", "C", "P", "C"]

k = 0
for i in s:
    if i == word[k]:
        k += 1
    if k == 4:
        print("I love UCPC")
        break
else:
    print("I hate UCPC")

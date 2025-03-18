import re

n = int(input())

# b: 이진수, o: 8진수, x: 16진수, d: 정수
b = format(n + 1, "b")[1:]
b = re.sub("0", "4", b)
b = re.sub("1", "7", b)
print(b)

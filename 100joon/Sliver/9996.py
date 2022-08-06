import sys

input = sys.stdin.readline
n = int(input())
s, e = map(str, input().rstrip().split("*"))

for _ in range(n):
    word = input().rstrip()
    if word[: len(s)] == s and word[-len(e) :] == e and len(word) >= len(s) + len(e):
        print("DA")
    else:
        print("NE")

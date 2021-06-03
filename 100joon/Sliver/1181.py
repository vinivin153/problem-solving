import sys


n = int(input())

word = {}
for i in range(n):
    a = sys.stdin.readline().rstrip()
    word[a] = len(a)


new_word = sorted(word.items(), key=lambda x: (x[1], x[0]))
for key, value in new_word:
    print(key)

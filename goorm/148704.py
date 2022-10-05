# 단어장 만들기
import sys

input = sys.stdin.readline
n, k = map(int, input().split())

words = []
for _ in range(n):
    words.append(input().rstrip())

words.sort(key=lambda x: (len(x), x))
print(words[k - 1])

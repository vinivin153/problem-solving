import sys

input = sys.stdin.readline

n, k = map(int, input().split())
words = []
for _ in range(n):
    word = input().rstrip()
    words.append(word[4:-4])

s = set(["a", "n", "t", "i", "c"])

ans = 0


def backtracking(cnt, q):
    global ans
    if cnt == k:
        temp = 0
        for word in words:
            for w in word:
                if w not in s:
                    break
            else:
                temp += 1

        if temp > ans:
            ans = temp

        return

    for i in range(q, 26):
        alpha = chr(ord("a") + i)
        if alpha not in s:
            s.add(alpha)
            backtracking(cnt + 1, i + 1)
            s.remove(alpha)


if k < 5:
    print(0)
else:
    backtracking(5, 1)
    print(ans)

# a n t i c -> 단어를 읽기 위한 최소 필수 글자

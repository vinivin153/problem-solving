"""
1. 두 단어가 같은 구성
2. 한 문자를 더하거나 뺏을 때 같은 구성
3. 한 문자를 바꿨을 때 같은 구성
"""

n = int(input())
ans = 0
word1 = input()
cnt_word1 = [0] * 26
for i in word1:
    cnt_word1[ord(i) - 65] += 1

for _ in range(n - 1):
    flag = 0
    cnt_word2 = [0] * 26
    word2 = input()
    for i in word2:
        cnt_word2[ord(i) - 65] += 1
    cnt = 0

    for i in range(26):
        if abs(cnt_word1[i] - cnt_word2[i]) >= 2:
            flag = 1
            break

        cnt += abs(cnt_word1[i] - cnt_word2[i])

    if flag:
        continue

    if cnt == 0 or cnt == 1:
        ans += 1

    if cnt == 2 and len(word1) == len(word2):
        ans += 1

print(ans)

# 비밀편지
import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    s = input().rstrip()
    v, token = map(str, input().rstrip().split())

    res = ""
    for i in range(len(s)):
        if v == "E":
            # 문자열 대소문자인 경우 변환
            if s[i].isupper():  # 대문자인 경우
                temp = ord(s[i]) + (ord(token[i % len(token)]) % 26)
                if temp > 90:
                    temp -= 26
                res += chr(temp)
            elif s[i].islower():
                temp = ord(s[i]) + (ord(token[i % len(token)]) % 26)
                if temp > 122:
                    temp -= 26
                res += chr(temp)
            else:
                res += s[i]
        else:
            if s[i].isupper():
                temp = ord(s[i]) - (ord(token[i % len(token)]) % 26)
                if temp < 65:
                    temp += 26
                res += chr(temp)
            elif s[i].islower():
                temp = ord(s[i]) - (ord(token[i % len(token)]) % 26)
                if temp < 97:
                    temp += 26
                res += chr(temp)
            else:
                res += s[i]
    print(res)

import sys

sys.setrecursionlimit(10**5)

s = input()
l = len(s)
ans = 0
visited = [False] * l


def stack(start):
    global ans
    cnt = 0
    i = start + 1
    while i < l:
        if visited[i]:
            continue

        visited[i] = True
        if s[i] == ")":
            if i - start == 1:
                return [1, i]
            else:
                ans += cnt + 1
                return [cnt, i]
        else:
            [c, k] = stack(i)
            cnt += c
            i = k
        i += 1


for i in range(l):
    if not visited[i] and s[i] == "(":
        stack(i)
print(ans)

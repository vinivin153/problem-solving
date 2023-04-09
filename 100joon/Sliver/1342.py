from collections import defaultdict

s = list(input())
s_len = len(s)

set_s = set()
visited = [False] * 11


def dfs(cnt, ss):
    if cnt == s_len:
        pre = "_"
        for i in ss:
            if i == pre:
                return
            pre = i
        set_s.add(ss)
        return

    for i in range(s_len):
        if not visited[i]:
            visited[i] = True
            dfs(cnt + 1, ss + s[i])
            visited[i] = False


dfs(0, "")
print(len(set_s))

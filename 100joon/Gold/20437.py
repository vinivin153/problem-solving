import sys
from collections import defaultdict, Counter

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input().rstrip()
    k = int(input())

    alpha = set([alpha for alpha, cnt in Counter(s).items() if cnt >= k])
    if not alpha:
        print(-1)
        continue

    alpha_idx = defaultdict(list)
    for idx, value in enumerate(s):
        if value in alpha:
            alpha_idx[value].append(idx)

    min_len, max_len = 10001, -1
    for i in alpha_idx.values():
        for j in range(k - 1, len(i)):
            min_len = min(min_len, i[j] - i[j - (k - 1)] + 1)
            max_len = max(max_len, i[j] - i[j - (k - 1)] + 1)

    print(min_len, max_len)

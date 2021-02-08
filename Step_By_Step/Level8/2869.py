a, b, v = map(int, input().split())
if (v - a) / (a - b) == (v - a) // (a - b):
    print(int((v - a) / (a - b) + 1))
else:
    print(((v - a) // (a - b) + 2))
# 계산실수.. v-a가 아니라 v-b가 나오면 더 깔끔한데

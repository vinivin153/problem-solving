n = int(input())
trees = list(map(int, input().split()))

hap = sum(trees)
limit = hap // 3
result = 0
if hap % 3 != 0:
    print("NO")
else:
    for tree in trees:
        result += tree // 2
    if result >= limit:
        print("YES")
    else:
        print("NO")

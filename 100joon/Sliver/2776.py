t = int(input())
for _ in range(t):
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr = set(arr1)
    m = int(input())
    arr2 = list(map(int, input().split()))

    for num in arr2:
        if num in arr:
            print(1)
        else:
            print(0)

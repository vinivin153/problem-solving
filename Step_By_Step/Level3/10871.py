a, b = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(a):
    if arr[i] < b:
        print(arr[i], end=" ")
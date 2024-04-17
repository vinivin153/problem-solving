n, k, b = map(int, input().split())
arr = [1] * (n + 1)

for _ in range(b):
    arr[int(input())] = 0

start = 1
end = k

count = sum(arr[1 : k + 1])
ans = count

while end < n:
    count -= arr[start]
    start += 1

    end += 1
    count += arr[end]

    if count > ans:
        ans = count

print(k - ans)

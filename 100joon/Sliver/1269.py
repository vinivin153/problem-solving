num_a, num_b = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = len(set(a + b))
print(c * 2 - num_a - num_b)

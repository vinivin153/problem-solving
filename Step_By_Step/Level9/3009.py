dict_x = {}
dict_y = {}
for i in range(3):
    x, y = map(int, input().split())
    if x in dict_x:
        dict_x[x] += 1
    else:
        dict_x[x] = 1
    if y in dict_y:
        dict_y[y] += 1
    else:
        dict_y[y] = 1

print(
    *[k for k, v in dict_x.items() if v == 1], *[k for k, v in dict_y.items() if v == 1]
)

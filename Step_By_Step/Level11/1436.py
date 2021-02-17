n = int(input())

cnt = 0
num = 666
while True:
    if "666" in str(num):
        cnt += 1
    if cnt == n:
        print(num)
        break
    if "6" in str(num // 100):
        num += 1
    else:
        num += 10

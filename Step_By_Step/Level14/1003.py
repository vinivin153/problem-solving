import sys

t = int(sys.stdin.readline())
dpzero = [0 for i in range(41)]
dpone = [0 for i in range(41)]

dpzero[0] = 1
dpone[1] = 1

for i in range(2, 41):
    dpzero[i] = dpzero[i - 1] + dpzero[i - 2]
    dpone[i] = dpone[i - 1] + dpone[i - 2]

for i in range(t):
    n = int(sys.stdin.readline())
    print(dpzero[n], dpone[n])

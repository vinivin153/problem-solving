a = input()
cnt = 0
i = 0
while i < len(a):
    if (
        "c=" in a[i : i + 2]
        or "c-" in a[i : i + 2]
        or "d-" in a[i : i + 2]
        or "lj" in a[i : i + 2]
        or "nj" in a[i : i + 2]
        or "s=" in a[i : i + 2]
        or "z=" in a[i : i + 2]
    ):
        cnt += 1
        i += 1
    elif "dz=" in a[i : i + 3]:
        cnt += 1
        i += 2
    else:
        cnt += 1
    i += 1
print(cnt)
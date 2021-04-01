def find_dwarf(dwarf):
    for i in range(8):
        for j in range(i + 1, 9):
            height = 0
            for k in range(9):
                if k != i and k != j:
                    height += dwarf[k]
            if height == 100:
                dwarf.remove(dwarf[j])
                dwarf.remove(dwarf[i])
                dwarf.sort()
                for x in dwarf:
                    print(x)
                exit(0)


dwarf = []

for _ in range(9):
    dwarf.append(int(input()))

find_dwarf(dwarf)

import sys

input = sys.stdin.readline
message = input().rstrip()
key = input().rstrip()

mat = [[""] * 5 for _ in range(5)]
pair = []
ans = []


def fill_mat():
    alpha = [False] * 26
    alpha[ord("J") - ord("A")] = True
    idx = 0

    for i in range(5):
        for j in range(5):
            while idx < len(key):
                if not alpha[ord(key[idx]) - ord("A")]:
                    mat[i][j] = key[idx]
                    alpha[ord(key[idx]) - ord("A")] = True
                    idx += 1
                    break
                else:
                    idx += 1

            else:
                for k in range(26):
                    if not alpha[k]:
                        alpha[k] = True
                        mat[i][j] = chr(65 + k)
                        break


def split_two_letters():
    i = 0
    end = len(message)
    while i < end:
        if i + 1 == end:
            pair.append(message[-1] + "X")
            break

        if message[i] == message[i + 1]:
            if message[i] == "X":
                pair.append(message[i] + "Q")
            else:
                pair.append(message[i] + "X")
            i += 1
        else:
            pair.append(message[i] + message[i + 1])
            i += 2


def encode():
    for p in pair:
        first = p[0]
        second = p[1]
        x1, y1, x2, y2 = 0, 0, 0, 0

        for i in range(5):
            for j in range(5):
                if mat[i][j] == first:
                    x1, y1 = i, j
                if mat[i][j] == second:
                    x2, y2 = i, j

        if x1 == x2:
            ans.append(mat[x1][(y1 + 1) % 5])
            ans.append(mat[x2][(y2 + 1) % 5])
        elif y1 == y2:
            ans.append(mat[(x1 + 1) % 5][y1])
            ans.append(mat[(x2 + 1) % 5][y2])
        else:
            ans.append(mat[x1][y2])
            ans.append(mat[x2][y1])


fill_mat()
split_two_letters()
encode()
print("".join(ans))

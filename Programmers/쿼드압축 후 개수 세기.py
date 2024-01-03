def solution(arr):
    count = [0, 0]
    for row in arr:
        for i in row:
            if i == 0:
                count[0] += 1
            else:
                count[1] += 1

    def divide(r, c, size):
        if size == 1:
            return

        first = arr[r][c]
        for i in range(r, r + size):
            for j in range(c, c + size):
                if arr[i][j] != first:
                    isDiff = True
                    t = size // 2
                    divide(r, c, t)
                    divide(r + t, c, t)
                    divide(r, c + t, t)
                    divide(r + t, c + t, t)
                    return

        count[first] += -(size**2) + 1

    divide(0, 0, len(arr[0]))
    return count

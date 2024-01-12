def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True, key=lambda x: x * 3)

    result = "".join(numbers)
    if result[0] == "0":
        return str(int(result))
    else:
        return result

def sort_files(files):
    result = []
    for idx, file in enumerate(files):
        for i in range(len(file)):
            if file[i].isdigit():
                head = file[:i]
                number = file[i : i + 5]
                for j in range(len(number)):
                    if not number[j].isdigit():
                        number = number[:j]
                        break
                result.append([idx, head, int(number)])
                break

    return sorted(result, key=lambda x: (x[1].lower(), x[2]))


def solution(files):
    f = sort_files(files)

    answer = []
    for i, _, _ in f:
        answer.append(files[i])

    return answer

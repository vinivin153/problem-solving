def solution(arr1, arr2):
    arr2 = [list(item) for item in zip(*arr2)]

    answer = [[] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            sum1 = 0
            for k in range(len(arr1[i])):
                sum1 += arr1[i][k] * arr2[j][k]
            answer[i].append(sum1)

    return answer

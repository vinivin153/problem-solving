# 동빈나 알고리즘 41.세그먼트 트리
# https://blog.naver.com/ndb796/221282210534

a = [1, 9, 3, 8, 4, 5, 5, 9, 10, 3, 4, 5]


# 리스트의 크기 결정
n = 1
while True:
    if len(a) < n * n:
        n = n * n * 2
        break
    n += 1
segmentTree = [0] * n

# 누적 합 트리 만들기
def init(start, end, idx):
    if start == end:
        segmentTree[idx] = a[start]
        return segmentTree[idx]

    mid = (start + end) // 2
    segmentTree[idx] = init(start, mid, idx * 2) + init(mid + 1, end, idx * 2 + 1)
    return segmentTree[idx]


# 구간 합 구하기
def prefix_sum(start, end, idx, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return segmentTree[idx]
    mid = (start + end) // 2
    return prefix_sum(start, mid, idx * 2, left, right) + prefix_sum(
        mid + 1, end, idx * 2 + 1, left, right
    )


# 특정 값이 변경된 경우( diff = 변경된 값 - 원래 값)
# 전체를 새로 업데이틑 하는 것이 아니라 범위 있는 값에 diff를 더해 업데이트
def update(start, end, idx, diff, diff_idx):
    if diff_idx > end or diff_idx < start:
        return
    segmentTree[idx] += diff
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, idx * 2, diff, diff_idx)
    update(mid + 1, end, idx * 2 + 1, diff, diff_idx)


init(0, 11, 1)
update(0, 11, 1, 1, 7)
print(prefix_sum(0, 11, 1, 4, 8))

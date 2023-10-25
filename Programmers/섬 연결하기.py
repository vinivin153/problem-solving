def solution(n, costs):
    costs.sort(key=lambda x: x[2])

    def find_parent(x):
        if parent[x] != x:
            return find_parent(parent[x])
        return parent[x]

    def union_parent(x, y):
        if x < y:
            parent[y] = x
        else:
            parent[x] = y

    total_cost = 0
    parent = [i for i in range(n)]

    for cost in costs:
        a, b, c = cost
        x = find_parent(a)
        y = find_parent(b)
        if x != y:
            union_parent(x, y)
            total_cost += c

    return total_cost

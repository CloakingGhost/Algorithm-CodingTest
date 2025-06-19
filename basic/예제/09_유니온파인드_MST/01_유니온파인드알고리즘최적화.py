def solution(n, queries):

    # def find(x):
    #     if x != parent[x]:
    #         parent[x] = find(parent[x])

    #     return parent[x]
    def find(x):
        root = x
        # 1. 대표 원소 찾기
        while root != parent[root]:
            root = parent[root]

        # 2. 경로 압축
        while x != parent[x]:
            parent[x] = root
            x = parent[x]

        return root

    def union(x, y):
        x_root = find(x)
        y_root = find(y)

        if x_root == y_root:
            return

        # if rank[x_root] > rank[y_root]:
        #     parent[y_root] = x_root
        # elif rank[x_root] < rank[y_root]:
        #     parent[x_root] = y_root
        # else:
        #     parent[x_root] = y_root
        #     rank[y_root] += 1

        if rank[x_root] > rank[y_root]:
            x_root, y_root = y_root, x_root

        parent[x_root] = y_root
        if rank[x_root] == rank[y_root]:
            rank[y_root] += 1

    answer = []
    parent = list(range(n + 1))
    rank = [0] * (n + 1)

    for query in queries:
        command, x, y = query
        if command == -1:
            union(x, y)
        else:
            if find(x) == find(y):
                answer.append(True)
            else:
                answer.append(False)

    return answer

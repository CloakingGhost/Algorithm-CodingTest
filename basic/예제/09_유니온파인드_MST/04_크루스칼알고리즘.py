# https://dailyalgo.kr/ko/problems/87


def solution(n, edges):

    def find(x):
        root = x
        while root != parent[root]:
            root = parent[root]

        while x != root:
            parent[x] = root
            x = parent[x]

        return root

    def union(x, y):
        x_root = find(x)
        y_root = find(y)

        if x_root == y_root:
            return False

        if rank[x_root] < rank[y_root]:
            x_root, y_root = y_root, x_root

        parent[y_root] = x_root
        if rank[x_root] == rank[y_root]:
            rank[x_root] += 1

        return True

    for i in range(len(edges)):
        edges[i].append(i + 1)

    edges.sort(key=lambda x: (x[-2], x[-1]))
    parent = list(range(n + 1))
    rank = [0] * (n + 1)

    edge_count = 0
    answer = []

    for x, y, w, idx in edges:
        if union(x, y):
            edge_count += 1
            answer.append(idx)
            if edge_count == n - 1:
                break
    return answer


print(
    solution(
        6,
        [
            [4, 3, 4],
            [1, 2, 3],
            [4, 6, 6],
            [1, 4, 10],
            [5, 6, 4],
            [3, 2, 2],
            [2, 4, 5],
            [6, 3, 1],
        ],
    )
)
print(solution(5, [[5, 2, 6], [3, 1, 2], [2, 3, 5], [2, 4, 6]]))

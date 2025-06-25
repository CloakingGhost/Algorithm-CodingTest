# https://dailyalgo.kr/ko/problems/89
def solution(n, syncs):
    def find(x):
        while x != parent[x]:  # 현 노드의 부모가 아니면
            parent[x] = parent[
                parent[x]
            ]  # 현 노드의 윗노드의 윗노드를 현 노드의 윗노드로 교체
            x = parent[x]

        return x

    def union(x, y):
        x_root = find(x)
        y_root = find(y)

        if x_root == y_root:
            return False

        if rank[x_root] > rank[y_root]:
            x_root, y_root = y_root, x_root

        parent[x_root] = y_root
        if rank[x_root] == rank[y_root]:
            rank[y_root] += 1

        return True

    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    edge_count = 0
    total = 0
    syncs.sort(key=lambda x: x[-1])

    for x, y, w in syncs:
        if union(x, y):
            edge_count += 1
            total += w

            if edge_count == n - 1:
                break

    return -1 if edge_count != n - 1 else total


print(
    solution(
        6,
        [[2, 4, 1], [5, 3, 5], [1, 5, 10], [4, 6, 12], [3, 2, 8], [5, 4, 9], [3, 4, 4]],
    )
)
print(solution(5, [[3, 2, 2], [5, 4, 6], [5, 1, 5], [2, 4, 4]]))
print(
    solution(
        9,
        [
            [8, 5, 9],
            [6, 7, 2],
            [9, 5, 1],
            [2, 3, 10],
            [7, 4, 6],
            [4, 9, 5],
            [5, 7, 7],
            [6, 8, 8],
            [4, 5, 3],
            [9, 7, 7],
            [9, 8, 2],
            [8, 7, 10],
            [4, 6, 7],
            [6, 9, 1],
            [6, 5, 7],
            [1, 2, 1],
        ],
    )
)

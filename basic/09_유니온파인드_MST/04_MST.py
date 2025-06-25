"""
신장트리(spanning tree)
1. 모든 정점이 간선을 통해 연결됨
2. 사이클이 없음


가중치의 합이 가장 작은 신장트리 == 최소신장트리

아이디어(크루스칼 알고리즘)
1. 가장 적은 비용의 간선을 선택                 -> 정렬
2. 잇고나서 사이클 판별                         -> 유니온-파인드
3. 사이클이 없으면 그냥 두고, 있으면 잇지 않음  -> E = V - 1
"""


def solution(n, edges):

    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x_root = find(x)
        y_root = find(y)

        # 사이클 존재
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
    # 1. 가중치에 따라 간선을 오름차순으로 정렬
    edges.sort(key=lambda x: x[-1])

    total = 0  # 비용의 총합
    count = 0  # 간선의 개수
    # 2. 가장 적은 비용의 간선부터 차례로 선택
    for x, y, w in edges:
        if union(x, y):  # 사이클이 없으면
            total += w
            count += 1

            if count == n - 1:
                break

    return total
